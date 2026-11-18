# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest00571(request):
    raw_body = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
