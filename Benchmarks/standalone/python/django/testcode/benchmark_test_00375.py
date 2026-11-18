# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00375(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body!s}'
    parsed = json.loads(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
