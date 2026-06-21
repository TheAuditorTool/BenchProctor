# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31254():
    xml_value = request.get_data(as_text=True)
    pending = list(str(xml_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
