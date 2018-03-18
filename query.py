import psycopg2
from time import strftime
dbname = "news"
query1 = ('''select articles.title, count(*) as num from articles JOIN log ON
	log.path like concat('/article/%',articles.slug)
	group by articles.title order by num desc limit 3;''')
query2 = ('''select authors.name, count(*) as num from authors join articles 
	on authors.id = articles.author
	JOIN log ON log.path LIKE concat('/article/%',articles.slug)
	GROUP BY authors.name order by num desc;''')
query3 = ('''select t.day, round(((e.errors::decimal)/ t.total), 3)*100 AS
	percent from (select date_trunc('day', time) "day", count(*) AS
	errors from log where status LIKE '404%' GROUP BY day) AS e join
	(select date_trunc('day', time) "day", count(*) AS total from log
	GROUP BY day) AS t ON t.day = e.day where
	(round(((e.errors::decimal) / t.total), 3)*100 > 1)
	ORDER BY percent desc;''')

print('Log Analysis Project')


def run(query):
	conn = psycopg2.connect("dbname="+dbname)
	cur = conn.cursor()
	cur.execute(query)
	rows = cur.fetchall()
	conn.close
	return rows


def popular_articles(q):
    print('\n')
    print("Question 1")
    print("What are the most popular 3 articles of all time?")
    result = run(q)
    i = 0
    for i in result:
        title = i[0]
        num_views = str(i[1])+" views"
        print(title+' - '+num_views)


def popular_authors(q):
    print('\n')
    print("Question 2")
    print("Who are the most popular article authors of all time?")
    result = run(q)
    i = 0
    for i in result:
        name = i[0]
        num_views = str(i[1])+" views"
        print(name+' - '+num_views)


def http_errors(q):
    print('\n')
    print("Question 3")
    print("On which days did more than 1% of requests lead to errors?")
    result = run(q)
    i = 0
    for i in result:
        day = i[0].strftime('%d-%m-%Y')
        per_errors = str(i[1])+" % errors"
        print(day+' - '+per_errors)


popular_articles(query1)
popular_authors(query2)
http_errors(query3)
