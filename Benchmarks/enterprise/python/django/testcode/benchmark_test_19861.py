# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19861(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    eval(str(data))
    return JsonResponse({"saved": True})
