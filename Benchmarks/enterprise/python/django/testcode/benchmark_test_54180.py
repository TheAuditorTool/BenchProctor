# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54180(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
