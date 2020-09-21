    Breve Descritivo do Projeto
Por limitações de hardware, simulações com instancias ec2 da plataforma de serviços Cloud da Amazon foram utilizadas.
O programa está incompleto, sendo cada arquivo "funções" independentes, porém correlatas ao todo.
Ao término dos testes unitários, a proposta é integrar as funcionalidades, realizar teste integrado, e finalizar a documentação de testes comprobatória.

    Pré-requisitos
Interpretador Python 3.

     Arquivos
FuncaoInput.py # Cria arquivo input e escreve informações
1CriacaoDeInstanciaEc2.py # Cria instancia ec2
2CriacaoDeInstanciaEc2SecurityGroupSpec.py # Cria regras para os grupos de segurança da instancia ec2
3CriacaoDeInstanciaEc2Volume.py # Cria e dimensiona o volume da instancia ec2
4CriacaoDeInstanciaEc2SSHParamiko.py # Acesso ssh a instancia ec2
CondicionalInicial.py # Condicional para criação do arquivo
LoginUserMenuSimples.py # Simples menu para posterior melhoria e interação com entrada de dados
StartStopInstancesEC2.py # Função para iniciar e parar as instancias, conforme tempo parametrizado.
     
    Autoria e contribuições
E. Ramello
https://docs.aws.amazon.com
