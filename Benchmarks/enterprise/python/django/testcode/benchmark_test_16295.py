# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16295(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % (upload_name,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return JsonResponse({"saved": True})
