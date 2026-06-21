# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53099(request):
    upload_name = request.FILES['upload'].name
    if upload_name not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = upload_name
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return JsonResponse({"saved": True})
