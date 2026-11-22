# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from pathlib import Path


def BenchmarkTest00064(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    Path(checked_path).write_text('data')
    return JsonResponse({"saved": True})
