# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77596(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
