reservations = conn.get_all_instances(instance_ids=[sys.argv[1]])
instances = [i for r in reservations for i in r.instances]
for i in instances:
    #Providencia chaves
    key_name = i.key_name 
    # Providencia Grupo de Seguranca
    security_group = i.groups[0].id
    # Providencia o tipo da instancia
    instance_type = i.instance_type
    print "A Instancia esta sendo criada"
    # Providencia id de subnet
    subnet_name = i.subnet_id
    # Finaliza criacao da instancia  
    reserve = conn.run_instances(image_id=ami_id,key_name=key_name,instance_type=instance_type,security_group_ids=[security_group],subnet_id=subnet_name)
