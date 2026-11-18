# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest00380(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = (lambda v: v.strip())(forwarded_ip)
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
