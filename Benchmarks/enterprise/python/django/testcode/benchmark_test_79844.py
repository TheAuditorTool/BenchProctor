# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79844(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
