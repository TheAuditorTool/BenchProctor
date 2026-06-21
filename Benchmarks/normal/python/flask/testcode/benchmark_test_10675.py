# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10675():
    user_id = request.args.get('id', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(user_id))
    return jsonify({"result": "success"})
