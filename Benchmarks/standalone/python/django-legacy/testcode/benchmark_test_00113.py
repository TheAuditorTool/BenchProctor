# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest00113(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value!s}'
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
