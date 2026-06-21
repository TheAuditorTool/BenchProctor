# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38671(request):
    upload_name = request.FILES['upload'].name
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
