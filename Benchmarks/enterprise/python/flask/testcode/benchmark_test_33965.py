# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest33965():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
