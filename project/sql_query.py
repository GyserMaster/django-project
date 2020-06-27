from django.db import connection


def id_sql(query="SELECT id FROM miapp_article WHERE title LIKE '%eget%'"):
    with connection.cursor() as cursor:
        queryset = []
        cursor.execute(query)
        row = cursor.fetchall()

        for array in row:
            for id in array:
                queryset.append(id)

    return queryset