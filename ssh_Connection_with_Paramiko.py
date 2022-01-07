from paramiko.client import SSHClient
import getpass

SSH_USER = input("Please provide Username: ")
SSH_PASS = getpass.getpass("Please provide Your Password: ")
SSH_HOST = input("Please provide the Host IP Address: ")
SSH_PORT = 22

client = SSHClient()

client.load_system_host_keys()
try:
    client.connect(SSH_HOST, port=SSH_PORT,
                             username=SSH_USER,
                             password=SSH_PASS,
                             look_for_keys=False)
    print("Connection Successfull!")
except Exception:
    print("Failed to Establish Connection. Please Try again.")

finally:
    client.close