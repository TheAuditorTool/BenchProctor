# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest68805():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    return Markup('<div>' + str(data) + '</div>')
