# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31533(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name}'
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return JsonResponse({'error': 'zero division'}, status=400)
    result = 100 / divisor
    return JsonResponse({"saved": True})
