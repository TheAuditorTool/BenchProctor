# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import base64


def BenchmarkTest22415(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
