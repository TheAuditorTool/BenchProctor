# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest32836():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    return Markup('<img src="' + str(data) + '">')
