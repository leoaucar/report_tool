#!/usr/bin/env python3

# Importar libraries necessárias
import psycopg2


# Função padrão para acessar o banco e executar uma query
def query_maker(query_needed):
    try:
        conn = psycopg2.connect("dbname=news")
    except:
        print("Unable to connect to the database")
    cur = conn.cursor()
    cur.execute(query_needed)
    result = cur.fetchall()
    conn.close()
    return result


# Dupla de funçoes que formatará os resultados das querys para melhor leitura
def format_result(query_result):
    result_string = ""
    for i in query_result:
        result_string += ("'" + str(i[1]) + "'" +
                          " with " + str(i[0]) +
                          " views" "\n")
    return result_string


def format_date(query_result):
    result_string = "The days with more than 1% of log errors are: \n"
    for i in query_result:
        result_string += ("Day: " + (str(i[0])) +
                          " with " + (str(round(i[3]*100, 3))) +
                          "% of errors")
    return result_string


# Busca os artigos mais populares
# Faz um count da quantidade de logs associados à uma determinada slug
# Para isso realiza um Join
top_articles_query = ("SELECT count(articles.title) as views, " +
                      "articles.title " +
                      "FROM log JOIN articles " +
                      "ON articles.slug = substring(log.path,10) " +
                      "GROUP BY articles.title ORDER BY views DESC;")
top_articles = query_maker(top_articles_query)

# Busca os autores mais populares
top_authors_query = ("SELECT count(authors.name) as views, authors.name " +
                     "FROM (articles JOIN log " +
                     "ON articles.slug = substring(log.path,10)) " +
                     "JOIN authors ON articles.author = authors.id " +
                     "GROUP BY authors.name ORDER BY views DESC;")
top_authors = query_maker(top_authors_query)

# Busca dias com + de 1% de erros nas requests
top_errors_query = ("SELECT t1.day, oks, wrongs," +
                    " wrongs::numeric/(wrongs+oks) as errors_share FROM " +
                    "(SELECT count(status) as oks, log.time::date as day " +
                    "FROM log WHERE status = '200 OK' GROUP BY day) " +
                    "as t1 LEFT JOIN " +
                    "(SELECT count(status) as wrongs, " +
                    "log.time::date as day " +
                    "FROM log WHERE status = '404 NOT FOUND' " +
                    "GROUP BY day) " +
                    "as t2 on t1.day = t2.day " +
                    "WHERE oks / 100 < wrongs;")
top_errors = query_maker(top_errors_query)


final_result = ("The most read articles are:\n" +
                format_result(top_articles) + "\n\n" +
                "The top authors are:\n" +
                format_result(top_authors) + "\n\n" +
                format_date(top_errors))


# Realizar print das querys
print(final_result)

# Extrair os resultados para um arquivo.txt
# Cria ou abre um arquivo txt
# Configura para sempre sobrescrever resultados pelos mais atuais
results = open("results.txt", "w")
results.write(final_result)
