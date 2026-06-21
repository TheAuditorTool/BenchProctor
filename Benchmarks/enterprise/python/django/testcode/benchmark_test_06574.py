# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06574(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
