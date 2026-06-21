# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest49432(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
