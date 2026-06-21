# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import redirect
import urllib.parse
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest32741():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
