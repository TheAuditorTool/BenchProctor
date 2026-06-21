# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest12372():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    return Markup('<img src="' + str(data) + '">')
