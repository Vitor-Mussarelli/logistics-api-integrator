import pyodbc
import datetime

# 1. Configuração da Conexão
def conectar_banco():
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=localhost;" # Ou o nome da sua instância
        "Database=DB_Integracao;"
        "Trusted_Connection=yes;"
    )
    return pyodbc.connect(dados_conexao)

# 2. Simulação de dados recebidos (JSON/Dicionário)
def simular_dados_api():
    return [
        {"id": 1001, "rastreio": "BR123456789", "cidade": "Araras", "status": "Em Trânsito", "valor": 25.50},
        {"id": 1002, "rastreio": "BR987654321", "cidade": "Limeira", "status": "Entregue", "valor": 18.90}
    ]

# 3. Processamento e Carga (ETL)
def carregar_dados():
    try:
        dados = simular_dados_api()
        conexao = conectar_banco()
        cursor = conexao.cursor()

        for item in dados:
            cursor.execute("""
                IF NOT EXISTS (SELECT 1 FROM tbd_Entregas_Integradas WHERE id_entrega = ?)
                BEGIN
                    INSERT INTO tbd_Entregas_Integradas (id_entrega, codigo_rastreio, cidade_destino, status_atual, valor_frete)
                    VALUES (?, ?, ?, ?, ?)
                END
            """, item['id'], item['id'], item['rastreio'], item['cidade'], item['status'], item['valor'])
        
        conexao.commit()
        print(f"Sucesso: {len(dados)} registros processados às {datetime.datetime.now()}")
    except Exception as e:
        print(f"Erro na integração: {e}")
    finally:
        cursor.close()
        conexao.close()

if __name__ == "__main__":
    carregar_dados()