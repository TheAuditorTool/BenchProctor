# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14780(request):
    upload_name = request.FILES['upload'].name
    data, _sep, _rest = str(upload_name).partition('\x00')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
