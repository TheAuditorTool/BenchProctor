# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest81432():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
