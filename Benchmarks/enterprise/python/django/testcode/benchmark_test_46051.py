# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def coalesce_blank(value):
    return value or ''

def BenchmarkTest46051(request):
    raw_body = request.body.decode('utf-8')
    data = coalesce_blank(raw_body)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
