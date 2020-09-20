
# Criacao do Volume (size, zone, snapshot=None, volume_type=None, iops=None)
# 1º argumento - Tamanho, 2º - Regiao, 3º - Tipo
vol = conn.create_volume(1, "us-west-1c", "ssd")
print 'Volume Id: ', vol.id # "Printa o id" o volume quando criado

# Anexa volume e exibe detalhes.
conn.attach_volume (vol.id, instance.id, "/dev/sdf")
print 'Attach Volume Result: ', result

