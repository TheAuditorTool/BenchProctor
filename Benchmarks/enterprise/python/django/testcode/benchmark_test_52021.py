# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest52021(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JsonResponse({'validated': str(processed)}, status=200)
    return JsonResponse({"saved": True})
