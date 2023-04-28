# BANDKAMP

<h4>BANDKAMP - Swagger Documentation: https://bandkamp-m5-s5.onrender.com/api/docs/swagger/</h4>
<h4>BANDKAMP - Redoc Documentation: https://bandkamp-m5-s5.onrender.com/api/docs/redoc/</h4>

#
<h4>NOTE:</h4>

Through this repository, I present the final result of the project that I developed for KenzieAcademy, in which I was tasked with modifying an existing project to promote improvements, as well as migrating the database from SQLite3 to Postgresql.

As I developed my work from a fork of a private repository, I am unable to make public the entirety of my development process and code changes leading up to the final result. If you are interested in reviewing the complete development process of this project in the repository where I originally developed this work, please do not hesitate to contact me. It would be my pleasure to present it to you. For now, I am providing a general overview of the project's objectives, requirements, and stages, as well as the final version of the work that I completed.
#

<h4>MAIN OBJECTIVES</h4>

The objective of this project was to update a music API that had been developed using APIView, base Serializer, and SQLite3 by transitioning it to use Generic View, Model Serializer, and Postgres instead of SQLite3. After successfully completing the migration, I integrated Postgres into the platform and developed API documentation in both swagger and redoc formats. The final version of the application was deployed using Render and is now available online at bandkamp-m5-s5.onrender.com.

<h4>ENTITY RELATIONSHIP DIAGRAM</h4>
![image](https://user-images.githubusercontent.com/106698505/235030808-631f2364-8391-4cac-9a64-8ee24435b065.png)


<h4>TASK 1:</h4>

A) Debugging:

Initially, the project had issues due to missing dependencies. My first task was to identify and correct these issues, as well as to address the code snippet that was causing the test failures in the application's failure logs.

Note: Throughout the project, tests for each app were carefully considered and used as a reference to ensure stability and functionality of the project.

B) Modeling:

After interpreting the application and understanding its routes and rules, I diagrammed the tables, their attributes, and relationships using dbdiagram.io and included a PNG of the ERD in the repository.

C) Migration to Postgres:

The original application was using the SQLite3 database, which I switched to Postgres, making the necessary configurations in the required files, such as settings.py, .env, and .env.example.

D) Model Serializer:

I switched the three serializers present in the application to ModelSerializer, without losing any characteristics, and renamed them respectively as AlbumSerializer, SongSerializer, and UserSerializer.

<h4>TASK 2:</h4>

Generic View:

In this task, my goal was to replace the UserView and UserDetailView (located in the directory users/views.py) from APIView to Generic View without altering any behavior.

<h4>TASK 3:</h4>

Generic View:

Similarly, in this task, my goal was to replace the AlbumView and SongView (located in the directories albums/views.py and songs/views.py) from APIView to Generic View without altering any behavior.

<h4>TASK 4:</h4>

A) Documentation:

I created an endpoint in the application (/api/docs/) that contains application documentation in both swagger and redoc formats.
Swagger: https://bandkamp-m5-s5.onrender.com/api/docs/swagger/
Redoc: https://bandkamp-m5-s5.onrender.com/api/docs/redoc/

B) Deployment:

Finally, I uploaded and made the application available through Render at bandkamp-m5-s5.onrender.com.


<h4>FINAL APPLICATION TESTS:</h4>

![image](https://user-images.githubusercontent.com/106698505/234953687-3a78817d-3163-4722-983a-728cf999b5aa.png)

#

# TO RUN THE APPLICATION LOCALLY OR RUN TEST PACKAGES:

- Verify if pytest and/or pytest-testdox packages are installed globally on your system:
```shell
pip list
```
- If "pytest" and/or "pytest-testdox" and/or "pytest-django" are listed in your global environment, use the following commands to uninstall them globally:
```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

After that, proceed with the steps:

1.Create your virtual environment:
```bash
python -m venv venv
```

2. Activate your venv:
```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate
```

3. Install the "pytest-testdox" package:
```shell
pip install pytest-testdox pytest-django
```

4. Now, just run the tests in the project root directory:
```shell
pytest --testdox -vvs
```

5. If you want a more concise log, just run the tests without the **verbose** flags:
```shell
pytest --testdox
```

<h4>Running tests in parts</h4>

If you want to run tests from a specific directory, you can use the following commands:

- Running user tests:
```python
pytest --testdox -vvs tests/users/
```

- Running album tests:
```python
pytest --testdox -vvs tests/albums/
```

-Running song tests:
```python
pytest --testdox -vvs tests/songs/
```

<!--

OBJETIVO GERAL DO PROJETO:

1. Neste projeto, utilizei um código legado de uma API de músicas desenvolvida com APIView, Serializer base e SQLite3, e fiz a transição deste aplicativo para Generic View, Model Serializer e utilização do Postgres no lugar do SQLite3.

2. Após finalizar a migração, já contando com o serviço de Postgres integrado a plataforma, e após realizar os ajustes conforme a proposta inicial, desenvolvi a documentação da API no formato swagger e também redoc, e finalizei o trabalho realizando o deploy da versão final da aplicação através do Render. A aplicação está online e disponível para uso através do link: bandkamp-m5-s5.onrender.com


TASK 1

A) Debug

Inicialmente o projeto contava com erros devido a algumas dependências ausentes. Minha primeira tarefa foi identificá-las e corrigi-las, bem como, ao verificar os logs de falha dos testes contidos na aplicação corrigi o trecho de código que estava originando a falha.

Importante: Após realizar os ajustes dos bugs iniciais e a transição para model serializer, os testes sobre cada app sempre foram levados em consideração e foram tomados como referência até a conclusão do projeto. A cada etapa e novo passo na reescrita do código e migração do banco de dados mantive os testes com funcionamento de 100% sobre cada app mantendo-os estáveis e comprovando o bom funcionamento do projeto, tal como foi concebido originalmente.


B) Modelagem

Tendo interpretado a aplicação e entendido as suas rotas e regras, diagramei as tabelas, seus atributos e relações, utilizando o dbdiagram.io, e incluí um PNG da DER no repositório.

C) Migração para Postgres

A aplicação legada estava utilizando o banco SQLite3. Realizei a troca para o Postgres, fazendo as devidas configurações nos arquivos necessários, como por exemplo, settings.py, .env e .env.example.

D) Model Serializer

Realizei a trocar dos 3 serializers presentes na aplicação para ModelSerializer, sem perder nenhuma característica. Os renomeei respectivamente como: AlbumSerializer, SongSerializer, UserSerializer.


TASK 2

Generic View - Meu objetivo nesta tarefa foi de substituir a UserView e a UserDetailView (diretório: users/views.py), de APIView para Generic View sem perder nenhum comportamento e/ou acrescentar.

TASK 3

Generic View - Meu objetivo nesta tarefa foi de substituir a AlbumView e a SongView (diretórios: albums/views.py e songs/views.py), de APIView  para Generic View sem perder nenhum comportamento e/ou acrescentar.


TASK 4

A) Documentação

Criei um endpoint na aplicação (/api/docs/), que contém a documentação da aplicação nos formatos swagger e redoc.

B) Deploy

Subi e disponibilizei a aplicação através o Render: bandkamp-m5-s5.onrender.com

 -->





<!--


# M5 - BandKamp Generic View

## Instalação dos pacotes de teste

- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:
```shell
pip list
```
- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:
```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate
```

3. Instale o pacote `pytest-testdox`:
```shell
pip install pytest-testdox pytest-django
```


4. Agora é só rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```

5. Caso queira um log mais resumido, basta executar com os testes sem as flags **verbose**:
```shell
pytest --testdox
```

## Rodando os testes por partes

Caso você tenha interesse em rodar apenas um diretório de testes específico, pode utilizar o comando:

- Rodando testes de users:
```python
pytest --testdox -vvs tests/users/
```

- Rodando testes de albums:
```python
pytest --testdox -vvs tests/albums/
```

- Rodando testes de songs:
```python
pytest --testdox -vvs tests/songs/
```

 -->
