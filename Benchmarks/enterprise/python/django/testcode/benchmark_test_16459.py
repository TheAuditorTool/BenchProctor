# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16459(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
