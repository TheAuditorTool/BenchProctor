# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03942(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
