# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00330(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
