# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41319(request):
    multipart_value = request.POST.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
