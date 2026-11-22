# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00214(request):
    upload_name = request.FILES['upload'].name
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    parsed = json.loads(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
