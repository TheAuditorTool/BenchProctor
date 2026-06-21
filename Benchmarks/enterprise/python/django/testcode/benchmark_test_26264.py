# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time


def to_text(value):
    return str(value).strip()

def BenchmarkTest26264(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = to_text(multipart_value)
    if time.time() > 1000000000:
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return JsonResponse({"saved": True})
