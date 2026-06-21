# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15630(request):
    raw_body = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
