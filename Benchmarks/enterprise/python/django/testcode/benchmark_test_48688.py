# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48688(request):
    multipart_value = request.POST.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
