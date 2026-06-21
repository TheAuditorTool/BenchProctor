# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46503(request):
    multipart_value = request.POST.get('multipart_field', '')
    int(str(multipart_value))
    return JsonResponse({"saved": True})
