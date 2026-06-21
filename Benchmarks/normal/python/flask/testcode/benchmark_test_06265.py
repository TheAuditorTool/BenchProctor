# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest06265():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    return Markup('<img src="' + str(data) + '">')
