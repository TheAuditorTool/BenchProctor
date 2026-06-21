# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65008(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    eval(str(data))
    return JsonResponse({"saved": True})
