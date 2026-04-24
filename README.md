# 🚚 Logistics API Integrator

Automatização de pipeline de dados logísticos utilizando Python e SQL Server. Este projeto demonstra a extração de dados de frete e rastreio simulando uma API (mock), realizando a validação e persistindo as informações em um banco de dados relacional para posterior consumo por Dashboards e ferramentas de BI (ex: Power BI).

## 🛠 Tecnologias Utilizadas
* **Python 3.x**: Linguagem principal para automação do fluxo.
* **SQL Server**: Banco de dados relacional para armazenamento estruturado.
* **Pyodbc**: Biblioteca para comunicação eficiente e segura entre a aplicação e o banco.

## ⚙️ Arquitetura e Fluxo
1. **Extração:** Simulação de requisição para consumo de dados operacionais (códigos de rastreios, cidades de destino e status atuais).
2. **Validação:** Verificação lógica dos dados em memória antes da inserção.
3. **Carga (Upsert):** Inserção inteligente dos registros no banco SQL Server utilizando comandos parametrizados (proteção contra SQL Injection) e tratamento de duplicidades.

## 🚀 Como Executar Localmente
1. Clone este repositório: `git clone https://github.com/seu-usuario/logistics-api-integrator.git`
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual e instale as dependências: `pip install -r requirements.txt`
4. Ajuste a string de conexão no arquivo `integradora.py` para o seu servidor SQL local.
5. Execute o script principal: `python integradora.py`

---
*Projeto desenvolvido por Vitor para demonstração prática de habilidades em integração de sistemas, banco de dados e automação de processos logísticos.*