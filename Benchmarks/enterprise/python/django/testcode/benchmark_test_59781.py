# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59781(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
