# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01337(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
