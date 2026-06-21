# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest04672():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    try:
        processed = int(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'forbidden'}), 400
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return jsonify({"result": "success"})
