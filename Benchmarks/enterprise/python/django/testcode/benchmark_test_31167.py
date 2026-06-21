# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31167(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
