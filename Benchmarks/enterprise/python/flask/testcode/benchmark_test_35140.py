# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest35140():
    xml_value = request.get_data(as_text=True)
    pending = list(str(xml_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
