# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49360(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if ua_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = ua_value
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
