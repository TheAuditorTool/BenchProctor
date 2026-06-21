# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19550(request):
    multipart_value = request.POST.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    eval(str(data))
    return JsonResponse({"saved": True})
