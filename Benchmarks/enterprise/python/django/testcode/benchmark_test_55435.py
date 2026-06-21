# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55435(request):
    upload_name = request.FILES['upload'].name
    eval(str(upload_name))
    return JsonResponse({"saved": True})
