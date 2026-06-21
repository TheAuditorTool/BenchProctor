# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import unicodedata
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest68303():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
