# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00289(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ' '.join(parts)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
