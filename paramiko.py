import paramiko
import json

class SSHHandler:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        """Establish the SSH connection."""
        try:
            self.connection = paramiko.SSHClient()
            self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.connection.connect(self.hostname, port=self.port, username=self.username, password=self.password)
        except paramiko.AuthenticationException:
            raise ValueError("Authentication failed, please verify your credentials")
        except paramiko.SSHException as e:
            raise ValueError(f"Could not establish SSH connection: {str(e)}")

    def execute_command(self, command, output_format='string'):
        """Execute SSH command and return the output."""
        if not self.connection:
            raise ValueError("Connection not established. Call connect() method first.")
        
        stdin, stdout, stderr = self.connection.exec_command(command)
        result = stdout.read().decode('utf-8')
        
        if output_format == 'json':
            try:
                return json.loads(result)
            except json.JSONDecodeError:
                raise ValueError("Output is not in JSON format")
        
        return result

    def transfer_to_remote(self, local_path, remote_path):
        """Transfer a file from the local machine to the remote machine."""
        if not self.connection:
            raise ValueError("Connection not established. Call connect() method first.")
        
        sftp = self.connection.open_sftp()
        sftp.put(local_path, remote_path)
        sftp.close()

    def transfer_from_remote(self, remote_path, local_path):
        """Transfer a file from the remote machine to the local machine."""
        if not self.connection:
            raise ValueError("Connection not established. Call connect() method first.")
        
        sftp = self.connection.open_sftp()
        sftp.get(remote_path, local_path)
        sftp.close()

    def close(self):
        """Terminate the SSH connection."""
        if self.connection:
            self.connection.close()


ssh = SSHHandler(hostname='example.com', port=22, username='user', password='password')

# Establish connection
ssh.connect()

# Execute command
output = ssh.execute_command('ls -la', output_format='string')
print(output)

# Transfer files
ssh.transfer_to_remote('local_file.txt', '/remote/path/remote_file.txt')
ssh.transfer_from_remote('/remote/path/remote_file.txt', 'local_file.txt')

# Close connection
ssh.close()
