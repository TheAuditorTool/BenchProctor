# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import sys
from django.http import HttpResponse


def BenchmarkTest07378(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    pending = list(str(argv_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
