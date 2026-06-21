# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def to_text(value):
    return str(value).strip()

def BenchmarkTest58370(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = to_text(multipart_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
