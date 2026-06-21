# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12356(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
