# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31900(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
