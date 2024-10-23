import paramiko 
from  requests import request
from django.shortcuts import render

def get_docker_status():
    
    hostname = "31.15.17.210"
    username = "apsiloon"
    password = "09224976231"

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddpolicy())
        client.connect(hostname ,username=username , password=password)

        stdin , stdout , stderr = client.exec_command('docker ps')
        docker_ps_output = stdout.read().decode("uft-8")

        client.close()

    except Exception as e:
        docker_ps_output = f"Error: {str(e)}"

    return render(request, 'docker_status/status.html',{"docker_ps_output" : docker_ps_output})
