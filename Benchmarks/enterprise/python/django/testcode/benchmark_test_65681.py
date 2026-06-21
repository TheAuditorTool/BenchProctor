# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65681(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % (host_value,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return JsonResponse({"saved": True})
