# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest70996():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    return Markup('<div>' + str(data) + '</div>')
