# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def BenchmarkTest60000(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % (host_value,)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
