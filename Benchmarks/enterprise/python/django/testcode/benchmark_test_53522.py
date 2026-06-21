# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53522(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
