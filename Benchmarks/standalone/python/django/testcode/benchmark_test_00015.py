# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest00015(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
