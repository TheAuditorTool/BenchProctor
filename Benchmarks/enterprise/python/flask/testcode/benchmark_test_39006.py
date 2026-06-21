# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest39006():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
