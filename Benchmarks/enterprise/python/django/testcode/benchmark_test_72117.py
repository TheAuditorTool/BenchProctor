# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72117(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = auth_header
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return JsonResponse({"saved": True})
