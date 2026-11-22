# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect
import json


def BenchmarkTest00013(request):
    host_value = request.META.get('HTTP_HOST', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    return redirect(str(data))
