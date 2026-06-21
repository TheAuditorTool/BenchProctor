# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34753(request):
    multipart_value = request.POST.get('multipart_field', '')
    exec(str(multipart_value))
    return JsonResponse({"saved": True})
