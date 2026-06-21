# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32889(request):
    multipart_value = request.POST.get('multipart_field', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(multipart_value))
    return JsonResponse({"saved": True})
