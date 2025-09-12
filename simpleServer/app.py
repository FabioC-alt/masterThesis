from http.server import BaseHTTPRequestHandler, HTTPServer
from kubernetes import client, config
import urllib.parse

PORT = 5000
DEPLOYMENT_NAME = "simple-server"
NAMESPACE = "default"

# Load in-cluster config
config.load_incluster_config()
apps_v1 = client.AppsV1Api()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)

        if self.path.startswith("/scale"):
            # Get 'replicas' parameter
            replicas = int(params.get("replicas", [1])[0])

            # Patch the deployment
            body = {"spec": {"replicas": replicas}}
            apps_v1.patch_namespaced_deployment_scale(
                name=DEPLOYMENT_NAME,
                namespace=NAMESPACE,
                body=body
            )

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(f"Scaled {DEPLOYMENT_NAME} to {replicas} replicas\n".encode())

        elif self.path.startswith("/pods"):
            # List pods
            v1 = client.CoreV1Api()
            pod_list = v1.list_namespaced_pod(namespace=NAMESPACE)
            pods = "\n".join([f"{pod.metadata.name}: {pod.status.phase}" for pod in pod_list.items])
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(pods.encode())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

if __name__ == "__main__":
    server = HTTPServer(("", PORT), Handler)
    print(f"Server running on port {PORT}")
    server.serve_forever()

