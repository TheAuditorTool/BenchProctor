# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57334(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    int(str(data))
    return JsonResponse({"saved": True})
