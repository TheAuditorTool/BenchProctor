# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62945(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    eval(str(data))
    return JsonResponse({"saved": True})
