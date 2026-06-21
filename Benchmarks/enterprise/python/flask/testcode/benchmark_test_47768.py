# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import re
from flask import request, jsonify
import ast


def BenchmarkTest47768():
    upload_name = request.files['upload'].filename
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    if not re.fullmatch('^[\\w\\s./\\[\\]\'\\"=_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
