# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34147(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
