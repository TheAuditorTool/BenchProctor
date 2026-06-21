# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest54195():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
