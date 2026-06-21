# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest49892():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    return Markup('<div>' + str(data) + '</div>')
