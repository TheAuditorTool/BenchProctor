# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62298(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    if str(data) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
