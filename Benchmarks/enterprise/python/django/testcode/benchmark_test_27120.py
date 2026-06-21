# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27120(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
