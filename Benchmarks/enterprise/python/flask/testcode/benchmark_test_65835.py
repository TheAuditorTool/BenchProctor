# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest65835(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
