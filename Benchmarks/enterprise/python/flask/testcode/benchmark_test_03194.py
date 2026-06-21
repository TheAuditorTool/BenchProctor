# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest03194():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return jsonify({"result": "success"})
