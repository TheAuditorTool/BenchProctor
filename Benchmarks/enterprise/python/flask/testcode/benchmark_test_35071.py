# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35071():
    raw_body = request.get_data(as_text=True)
    data = '%s' % (raw_body,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
