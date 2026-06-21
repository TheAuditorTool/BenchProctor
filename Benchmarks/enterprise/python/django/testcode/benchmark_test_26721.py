# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest26721(request):
    multipart_value = request.POST.get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
