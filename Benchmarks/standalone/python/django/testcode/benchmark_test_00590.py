# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect
import json


def BenchmarkTest00590(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = json_value if json_value else 'default'
    return redirect(str(data))
