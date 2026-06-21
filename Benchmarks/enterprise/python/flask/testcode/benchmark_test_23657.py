# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest23657():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    return Markup('<img src="' + str(data) + '">')
