# SPDX-License-Identifier: Apache-2.0
import logging
import re
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest56326():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = FormData(payload=prop_value).payload
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
