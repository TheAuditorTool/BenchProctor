# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52299(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    int(str(data))
    return JsonResponse({"saved": True})
