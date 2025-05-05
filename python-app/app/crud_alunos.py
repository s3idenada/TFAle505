import logging
import psycopg2
from psycopg2 import sql, Error

# Configuração do sistema de logs
logging.basicConfig(
    filename='escola_infantil.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Função para conectar ao banco de dados
def conectar():
    try:
        conn = psycopg2.connect(
            dbname="escola_infantil",
            user="postgres",
            password="cursoads1",
            host="localhost",
            port="5432"
        )
        return conn
    except Error as e:
        logging.critical(f"Erro ao conectar ao banco de dados: {e}")
        raise

# Função CREATE
def criar_aluno(nome, idade, turma):
    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "INSERT INTO alunos (nome, idade, turma) VALUES (%s, %s, %s) RETURNING id;"
        cursor.execute(query, (nome, idade, turma))
        aluno_id = cursor.fetchone()[0]
        conn.commit()
        logging.info(f"CREATE: Aluno {{'nome': '{nome}', 'idade': {idade}, 'turma': '{turma}'}} inserido com sucesso. ID gerado: {aluno_id}")
        return aluno_id
    except Error as e:
        logging.error(f"CREATE: Erro ao inserir novo aluno - {e}")
        raise
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()

# Função READ
def listar_alunos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "SELECT * FROM alunos;"
        cursor.execute(query)
        alunos = cursor.fetchall()
        logging.info("READ: Listagem de todos os alunos solicitada.")
        return alunos
    except Error as e:
        logging.error(f"READ: Erro ao listar alunos - {e}")
        raise
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()

# Função UPDATE
def atualizar_aluno(aluno_id, nome=None, idade=None, turma=None):
    try:
        conn = conectar()
        cursor = conn.cursor()
        campos = []
        valores = []
        if nome:
            campos.append("nome = %s")
            valores.append(nome)
        if idade:
            campos.append("idade = %s")
            valores.append(idade)
        if turma:
            campos.append("turma = %s")
            valores.append(turma)
        valores.append(aluno_id)
        query = sql.SQL(f"UPDATE alunos SET {', '.join(campos)} WHERE id = %s;")
        cursor.execute(query, valores)
        conn.commit()
        logging.info(f"UPDATE: Aluno com ID '{aluno_id}' atualizado: {{'nome': '{nome}', 'idade': {idade}, 'turma': '{turma}'}}.")
    except Error as e:
        logging.error(f"UPDATE: Erro ao atualizar aluno com ID '{aluno_id}' - {e}")
        raise
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()

# Função DELETE
def deletar_aluno(aluno_id):
    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "DELETE FROM alunos WHERE id = %s;"
        cursor.execute(query, (aluno_id,))
        if cursor.rowcount == 0:
            logging.error(f"DELETE: Falha ao deletar aluno com ID '{aluno_id}' - Aluno não encontrado no banco de dados.")
        else:
            conn.commit()
            logging.info(f"DELETE: Aluno com ID '{aluno_id}' removido com sucesso.")
    except Error as e:
        logging.error(f"DELETE: Erro ao deletar aluno com ID '{aluno_id}' - {e}")
        raise
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()