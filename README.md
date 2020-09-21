    Breve Descritivo do Projeto
Por limitações de hardware, simulações com instancias ec2 da plataforma de serviços Cloud da Amazon foram utilizadas.   <br/>
O programa está incompleto, sendo cada arquivo "funções" independentes, porém correlatas ao todo.   <br/>
Ao término dos testes unitários, a proposta é integrar as funcionalidades, realizar teste integrado, e finalizar a documentação de testes comprobatória.   <br/>

    Pré-requisitos
Interpretador Python 3.

     Arquivos
FuncaoInput.py # Cria arquivo input e escreve informações   <br/>
1CriacaoDeInstanciaEc2.py # Cria instancia ec2  <br/>
2CriacaoDeInstanciaEc2SecurityGroupSpec.py # Cria regras para os grupos de segurança da instancia ec2   <br/>
3CriacaoDeInstanciaEc2Volume.py # Cria e dimensiona o volume da instancia ec2   <br/>
4CriacaoDeInstanciaEc2SSHParamiko.py # Acesso ssh a instancia ec2   <br/>
CondicionalInicial.py # Condicional para criação do arquivo   <br/>
LoginUserMenuSimples.py # Simples menu para posterior melhoria e interação com entrada de dados   <br/>
StartStopInstancesEC2.py # Função Lambda para iniciar e parar as instancias ec2 AWS, conforme tempo parametrizado e interação por Tag'sID.  <br/>
     
   <br/>
https://docs.aws.amazon.com
