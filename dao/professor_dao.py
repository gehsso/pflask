from dao.db_config import get_connection

class ProfessorDAO:
    
    sqlSelect = 'select id, nome, disciplina from professor'
    
    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        return lista