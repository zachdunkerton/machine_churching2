import re
import os
import sys
import sqlite3
import pandas as pd

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
def query(conn, sql):
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    return pd.DataFrame(results)
def get_top_ref(text, verses):
    distances = verses.word.apply(lambda x: len(list(set(text.split(' ')).intersection(x.split(' ')))))
    refs = []
    for ref in distances.sort_values(ascending = False)[1:25].index:
        refs.append(ref)
    return refs
def array_to_string(refs):
    ref_string = ''
    for ref in refs:
        ref_string +=  ref+ ','
    return ref_string
def spacing(x):
    verse = ''
    for word in x.values:
        verse += word + ' '
    return verse