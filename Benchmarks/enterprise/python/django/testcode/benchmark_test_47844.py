# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47844(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
