# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00246(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    if match is None:
        return JsonResponse({'error': 'not an email address'}, status=400)
    domain = match.group(1)
    return JsonResponse({'domain': domain}, status=200)
