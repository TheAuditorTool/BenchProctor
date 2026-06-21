# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48814(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
