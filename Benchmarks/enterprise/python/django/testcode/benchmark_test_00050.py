# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import base64


def BenchmarkTest00050(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
