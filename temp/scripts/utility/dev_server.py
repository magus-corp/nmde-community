import http.server
import socketserver
import os

# Get the absolute path of the script itself
script_path = os.path.abspath(__file__)

# Get the directory where the script is located
script_dir = os.path.dirname(script_path)

# We assume the script is in .../scripts/utility, and we want to serve from the repo root.
# So we go up two directories.
repo_root = os.path.abspath(os.path.join(script_dir, '..', '..'))

# Change the current working directory to the repository root
os.chdir(repo_root)

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving HTTP on port {PORT} from directory {os.getcwd()}...")
    print("You can now access the files at http://<your-ip-address>:8000")
    print("To install on a new node, you can use a command like:")
    print("curl -sSL http://<your-ip-address>:8000/scripts/install/install_this_repo | bash")
    httpd.serve_forever()
