import boto3
import botocore
import paramiko
# Salve a chave
key = paramiko.RSAKey.from_private_key_file(path/to/mykey.pem)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Conectando
try:
    # username = usuario e istance ip = ip publico da instancia 
    client.connect(hostname=instance_ip, username="ubuntu", pkey=key)

    # Comando apos conectar
    stdin, stdout, stderr = client.exec_command(cmd)
    print stdout.read()

    # Fechar conexao e servico
    client.close()
    break

except Exception, e:
    print e
