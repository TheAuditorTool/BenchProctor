# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02089():
    xml_value = request.get_data(as_text=True)
    pending = list(str(xml_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return jsonify({'error': 'zero division'}), 400
    result = 100 / divisor
    return jsonify({"result": "success"})
