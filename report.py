#importar libraries necessárias
import psycopg2


#função padrão para acessar o banco e executar uma query
def query_maker(query_needed):
    try:
        conn = psycopg2.connect("dbname=news")
    except:
        print ("Unable to connect to the database")
    cur = conn.cursor()
    cur.execute(query_needed)
    result = cur.fetchall()
    conn.close()
    return result

#busca os artigos mais populares
#Faz um count da quantidade de logs associados à uma determinada slug
#para isso realiza um Join
top_articles_query ="SELECT count(articles.title) as views, articles.title FROM log JOIN articles ON articles.slug = substring(log.path,10) GROUP BY articles.title ORDER BY views DESC;"
top_articles = query_maker(top_articles_query)

#busca os autores mais populares
top_authors_query = "SELECT count(authors.name) as views, authors.name FROM (articles JOIN log on articles.slug = substring(log.path,10)) JOIN authors ON articles.author = authors.id GROUP BY authors.name ORDER BY views DESC"
top_authors = query_maker(top_authors_query)

#busca dias com + de 1% de erros nas requests
top_errors_query = "SELECT count(status), status, log.time::date as day FROM log GROUP BY day, status HAVING count(status = '404 NOT found') < count(status = '200 OK');"
top_errors = query_maker(top_errors_query)

final_result = ("The most read articles are:\n" +
str(top_articles) + "\n\n" +
"The top authors are:\n" +
str(top_authors) + "\n\n" +
"The days with more than 1% of errors are:\n" +
str(top_errors))


#realizar print das querys
print(final_result)

#extrair os resultados para um arquivo.txt
#cria ou abre um arquivo txt e configura para sempre sobrescrever resultados pelos mais atuais
results = open("results.txt","w")
results.write(final_result)
