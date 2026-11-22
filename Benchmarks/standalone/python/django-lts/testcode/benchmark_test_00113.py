# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00113(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parsed = json.JSONDecoder().decode(str(header_value))
    return JsonResponse({'parsed': str(parsed)}, status=200)
