# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33682(request):
    multipart_value = request.POST.get('multipart_field', '')
    if str(multipart_value) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
