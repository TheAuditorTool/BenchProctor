# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest17120():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    return Markup('<img src="' + str(data) + '">')
