#responder:
#1. Quais são os três artigos mais populares de todos os tempos?
#2. Quem são os autores de artigos mais populares de todos os tempos?
#3. Em quais dias mais de 1% das requisições resultaram em erros?

#importar libraries necessárias
import psycopg2


#função de report
def query_maker(query_needed):
#criar conexão com banco de dados
    try:
        conn = psycopg2.connect("dbname=news")
    except:
        print ("Unable to connect to the database")
    cur = conn.cursor()
#executar query de select
    cur.execute(query_needed)
    result = cur.fetchall()
#encerrar conexão
    conn.close()
#retorna resultados para serem usados
    return result

#chamar a função para querys distintas
test_string = "SELECT * from authors LIMIT 5;"
top_authors = query_maker(test_string)
#realizar print das querys
print(top_authors)

#extrair os resultados para um arquivo.txt
