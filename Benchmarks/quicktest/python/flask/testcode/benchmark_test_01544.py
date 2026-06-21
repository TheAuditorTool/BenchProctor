# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import defusedxml.ElementTree
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest01544():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
