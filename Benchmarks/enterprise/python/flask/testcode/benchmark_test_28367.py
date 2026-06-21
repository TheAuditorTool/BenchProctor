# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest28367():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return jsonify({"result": "success"})
