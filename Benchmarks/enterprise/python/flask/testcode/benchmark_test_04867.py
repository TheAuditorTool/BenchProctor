# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest04867():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    return Markup('<div>' + str(data) + '</div>')
