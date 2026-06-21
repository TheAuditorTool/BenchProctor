# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11550(request):
    multipart_value = request.POST.get('multipart_field', '')
    values = str(multipart_value).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
