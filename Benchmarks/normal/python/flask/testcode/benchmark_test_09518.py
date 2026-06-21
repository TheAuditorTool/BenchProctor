# SPDX-License-Identifier: Apache-2.0
import unicodedata
from app_runtime import db


def BenchmarkTest09518():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % (db_value,)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
