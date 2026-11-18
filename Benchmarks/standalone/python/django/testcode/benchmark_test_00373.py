# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect
import json


def BenchmarkTest00373(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    return redirect(str(data))
