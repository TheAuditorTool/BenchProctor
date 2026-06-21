# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70992(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    eval(str(data))
    return JsonResponse({"saved": True})
