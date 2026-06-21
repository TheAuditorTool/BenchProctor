# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35384(request):
    upload_name = request.FILES['doc'].name
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
