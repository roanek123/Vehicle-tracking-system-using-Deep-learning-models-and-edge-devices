import os
import paramiko

def scp_transfer(remote_host, username, password, remote_file):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        ssh.connect(remote_host, username=username, password=password)
        
        scp = paramiko.SFTPClient.from_transport(ssh.get_transport())
        
        # Get the directory of the Python script
        script_dir = os.path.dirname(os.path.realpath(__file__))
        
        # Construct the local path with the 'received' folder
        received_folder = os.path.join(script_dir, 'received')
        os.makedirs(received_folder, exist_ok=True)  # Create 'received' folder if it doesn't exist
        local_path = os.path.join(received_folder, os.path.basename(remote_file))
        
        scp.get(remote_file, local_path)
        
        print("File transferred successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        scp.close()
        ssh.close()

if __name__ == "__main__":
    remote_host = '192.168.125.108'
    username = 'bhalu'
    password = 'bhalu'
    remote_file = '/home/bhalu/project/capture/test.h264'

    scp_transfer(remote_host, username, password, remote_file)
