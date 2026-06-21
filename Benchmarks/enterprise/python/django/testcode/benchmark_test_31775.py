# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest31775(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
