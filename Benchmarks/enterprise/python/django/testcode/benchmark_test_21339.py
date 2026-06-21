# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21339(request):
    upload_name = request.FILES['upload'].name
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
