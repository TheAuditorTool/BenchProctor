# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80950(request):
    multipart_value = request.POST.get('multipart_field', '')
    if len(str(multipart_value)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
