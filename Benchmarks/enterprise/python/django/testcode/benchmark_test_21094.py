# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
import os


def relay_value(value):
    return value

def BenchmarkTest21094(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = relay_value(json_value)
    if os.environ.get("APP_ENV", "production") != "test":
        return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
    return JsonResponse({"saved": True})
