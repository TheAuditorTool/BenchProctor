# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79769(request):
    upload_name = request.FILES['upload'].name
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    eval(str(data))
    return JsonResponse({"saved": True})
