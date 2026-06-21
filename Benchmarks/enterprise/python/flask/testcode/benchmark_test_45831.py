# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest45831():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '{}'.format(forwarded_ip)
    return Markup('<img src="' + str(data) + '">')
