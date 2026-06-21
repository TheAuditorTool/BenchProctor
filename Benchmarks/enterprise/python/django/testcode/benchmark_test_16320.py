# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest16320(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = f'{forwarded_ip:.200s}'
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
