# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77579(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
