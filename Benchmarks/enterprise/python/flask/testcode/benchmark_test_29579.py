# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest29579():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
