# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05124():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    exec(str(processed))
    return jsonify({"result": "success"})
