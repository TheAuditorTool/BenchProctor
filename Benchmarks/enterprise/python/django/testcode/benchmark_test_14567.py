# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14567(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
