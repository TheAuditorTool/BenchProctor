# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest67918(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
