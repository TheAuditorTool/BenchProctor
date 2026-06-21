# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46053(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
