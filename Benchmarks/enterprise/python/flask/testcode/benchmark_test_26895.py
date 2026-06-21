# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest26895():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
