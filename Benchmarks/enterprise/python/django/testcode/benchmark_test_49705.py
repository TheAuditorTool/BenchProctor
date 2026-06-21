# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49705(request):
    multipart_value = request.POST.get('multipart_field', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(multipart_value))
    return JsonResponse({"saved": True})
