# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58292(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
