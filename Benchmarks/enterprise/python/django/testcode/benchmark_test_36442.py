# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import sys
from django.http import HttpResponse
import json


def BenchmarkTest36442(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    try:
        data = json.loads(argv_value).get('value', argv_value)
    except (json.JSONDecodeError, AttributeError):
        data = argv_value
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('/var/app/data/' + str(processed), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
