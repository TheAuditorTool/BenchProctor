# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64652(request):
    multipart_value = request.POST.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    if str(data) in ('localhost', 'internal-gateway'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
