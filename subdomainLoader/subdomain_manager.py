import subprocess
import os

class SubdomainManager:
    def __init__(self, domain):
        self.domain = domain

    def create_subdomain_folder(self, subdomain):
        path = f"/var/www/{subdomain}.{self.domain}/html"
        os.makedirs(path, exist_ok=True)
        return path

    def configure_nginx(self, subdomain):
        config_path = f"/etc/nginx/sites-available/{subdomain}.{self.domain}"
        config_content = f"""
        server {{
            listen 80;
            server_name {subdomain}.{self.domain};
            root /var/www/{subdomain}.{self.domain}/html;
            index index.html;
        }}
        """
        with open(config_path, 'w') as config_file:
            config_file.write(config_content)
        subprocess.run(["ln", "-sf", config_path, f"/etc/nginx/sites-enabled/{subdomain}.{self.domain}"])

    def apply_ssl(self, subdomain):
        subprocess.run(["certbot", "--nginx", "-d", f"{subdomain}.{self.domain}"], check=True)

    def reload_nginx(self):
        subprocess.run(["systemctl", "reload", "nginx"], check=True)
