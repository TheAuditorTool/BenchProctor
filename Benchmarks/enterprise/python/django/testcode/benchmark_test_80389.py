# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80389(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    exec(str(data))
    return JsonResponse({"saved": True})
