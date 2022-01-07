from paramiko.client import AutoAddPolicy, SSHClient
import getpass

SSH_USER = input("Please provide Username: ")
#SSH_PASS = getpass.getpass("Please provide Your Password: ") # or
SSH_PASS = getpass.getpass(prompt="Please Provide your Password: ", stream=None)
SSH_HOST = input("Please provide the Host IP Address: ")
SSH_PORT = 22

client = SSHClient()
# this add new client host key not really a good idea for security reason
client.set_missing_host_key_policy(AutoAddPolicy())

client.load_system_host_keys()
try:
    client.connect(SSH_HOST, port=SSH_PORT, username=SSH_USER, password=SSH_PASS, look_for_keys=False)
    print("Connection Successfull!")
except Exception:
    print("Failed to Establish Connection. Please Try again.")

finally:
    client.close