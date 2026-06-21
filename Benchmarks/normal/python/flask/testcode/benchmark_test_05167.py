# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest05167():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    return Markup('<img src="' + str(data) + '">')
