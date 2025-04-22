# DAG - Atividade prática: Desenvolvimento em Cloud Aplicada

Este projeto contém uma DAG desenvolvida no Apache Airflow com o objetivo de aplicar conhecimentos sobre construção de pipelines, operadores diversos e uso de XCom e branching.

## 📋 Descrição

A DAG realiza as seguintes operações:

- Log inicial com PythonOperator
- Listagem de arquivos no diretório via BashOperator
- Execução de consulta em banco de dados PostgreSQL com PostgresHook
- Decisão condicional usando BranchPythonOperator
- Execução de um dos caminhos (A ou B)
- Finalização com um EmptyOperator

[![Assista a demonstração](.github/screenshots/demo.mp4)](.github/screenshots/demo.mp4)

## 🛠️ Tecnologias e Ferramentas

- Python 3.10+
- Apache Airflow
- Docker + Docker Compose (para Postgres)
- PostgreSQL

## 🚀 Setup do Projeto

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local:

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DA_PASTA>
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt

```


### 4. Configure as variáveis de ambiente
```bash
source setup.sh

```

Este script define variáveis como:

- AIRFLOW_HOME
- AIRFLOW__CORE__DAGS_FOLDER
- AIRFLOW__CORE__PLUGINS_FOLDER
- AIRFLOW__DATABASE__SQL_ALCHEMY_CONN

### 5. Inicie o PostgreSQL com Docker (opcional)

Certifique-se de que o Docker está instalado e rodando, então execute:

```bash
docker compose up -d
```

Isso iniciará um container com um banco PostgreSQL acessível pelo Airflow. A DAG usa a conexão default com o postgres, atualize os dados de conexão no Airflow se necessário.

### 6. Execute o Airflow em modo standalone

```bash
airflow standalone
```

A interface web estará disponível em: http://localhost:8080
Usuário e senha padrão serão exibidos no terminal ao rodar o comando acima.


Desenvolvido por Alisson Costa para a disciplina de Desenvolvimento em Cloud Aplicada.


