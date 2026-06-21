# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45516(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    eval(str(data))
    return JsonResponse({"saved": True})
