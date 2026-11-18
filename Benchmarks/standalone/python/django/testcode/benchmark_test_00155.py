# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00155(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ' '.join(str(auth_header).split())
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
