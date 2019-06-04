from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import os, sqlite3


def get_db():
    # open db
    conn = sqlite3.connect(os.path.join(settings.MEDIA_ROOT, 'billboard.db'))
    cursor = conn.cursor()

    # try create new table
    try:
        cursor.execute("""CREATE TABLE DATA
        (
            SLOT INTEGER NOT NULL PRIMARY KEY,
            DATA TEXT
        );""")
    except:
        pass

    return conn, cursor


def billboard(request):
    op = request.GET.get('op')
    try:
        op = int(request.GET['op'])
        assert 0 <= op <= 2
    except:
        return HttpResponse(b'')
    op = int(op)
    conn, cursor = get_db()

    if op == 0:
        result = cursor.execute('select * from data').fetchall()
        print(result)
        conn.close()
        return render(request, 'billboard.html', locals())

    content = request.GET.get('data', '')
    response = {'op': op}

    # output data
    try:
        cursor.execute("insert into data (slot,data) values (?,?);", [op, content])
        response['succ'] = 1
    except:
        try:
            cursor.execute("update data set data=? where slot=?;", [content, op])
            response['succ'] = 2
        except:
            response['succ'] = 0

    # close db
    conn.commit()
    print(cursor.execute('select * from data').fetchall())
    conn.close()

    return JsonResponse(response)
