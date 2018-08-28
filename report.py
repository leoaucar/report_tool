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

#busca os artigos mais populares
#Faz um count da quantidade de logs associados à uma determinada slug
#para isso realiza um Join
top_articles_query ="SELECT count(*) as views, articles.title FROM log JOIN articles ON articles.slug = substring(log.path,10) GROUP BY articles.title ORDER BY views DESC;"
top_articles = query_maker(top_articles_query)

#busca os autores mais populares
top_authors_query = "SELECT * from authors LIMIT 1;"
top_authors = query_maker(top_authors_query)

#busca dias com + de 1% de erros nas requests
top_errors_query = "SELECT * from log LIMIT 1;"
top_errors = query_maker(top_errors_query)


#realizar print das querys
print("The most read articles are:\n" +
str(top_articles) + "\n\n" +
"The top authors are:\n" +
str(top_authors) + "\n\n" +
"The days with more than 1% of errors are:\n" +
str(top_errors)
)

#extrair os resultados para um arquivo.txt
#cria ou abre um arquivo txt e configura para sempre sobrescrever resultados pelos mais atuais
results = open("results.txt","w")
results.write(str(top_articles) + str(top_errors) + str(top_authors))
