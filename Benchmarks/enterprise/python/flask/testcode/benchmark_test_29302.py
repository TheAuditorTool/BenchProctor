# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import sys
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest29302():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = FormData(payload=argv_value).payload
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
