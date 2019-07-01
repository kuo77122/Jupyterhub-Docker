import os
import sys
from oauthenticator.github import GitHubOAuthenticator

c.JupyterHub.authenticator_class = GitHubOAuthenticator

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.JupyterHub.hub_ip = os.environ['HUB_IP']

c.JupyterHub.services = [
    {
        'name': 'cull-idle',
        'admin': True,
        'command': [sys.executable, 'cull_idle_servers.py', '--timeout=3600'],
    }
]
# Redirect to JupyterLab, instead of the plain Jupyter notebook
c.Spawner.default_url = '/lab'
