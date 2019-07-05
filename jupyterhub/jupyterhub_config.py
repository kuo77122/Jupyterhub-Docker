import os
import sys
from oauthenticator.github import GitHubOAuthenticator

# GitHubOauth
c.JupyterHub.authenticator_class = GitHubOAuthenticator
c.Authenticator.admin_users = {'kuo77122'}
c.GitHubOAuthenticator.oauth_callback_url = 'https://jupyterhub.nanpower.me/hub/oauth_callback'
c.GitHubOAuthenticator.client_id = os.environ['GITHUB_OAUTH_ID']
c.GitHubOAuthenticator.client_secret = os.environ['GITHUB_OAUTH_SECRET']

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# Connect containers to this Docker network
network_name = os.environ['DOCKER_NETWORK_NAME']
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name
c.DockerSpawner.extra_host_config = { 'network_mode': network_name }

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

# JupyterHub Cull Idle
c.JupyterHub.services = [
    {
        'name': 'cull-idle',
        'admin': True,
        'command': [sys.executable, 'cull_idle_servers.py', '--timeout=3600'],
    }
]
# Redirect to JupyterLab, instead of the plain Jupyter notebook
c.Spawner.default_url = '/lab'

# Resources limitation
c.Spawner.mem_limit = '1G'
