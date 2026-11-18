# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest00643(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parsed = yaml.safe_load(origin_value)
    return JsonResponse({'parsed': str(parsed)}, status=200)
