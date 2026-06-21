# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70406(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
