# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68327(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if header_value:
        data = header_value
    else:
        data = ''
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
