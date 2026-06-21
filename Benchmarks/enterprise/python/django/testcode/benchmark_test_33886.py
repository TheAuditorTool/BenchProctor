# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33886(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    exec(str(data))
    return JsonResponse({"saved": True})
