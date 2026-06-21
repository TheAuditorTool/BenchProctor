# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66442(request):
    upload_name = request.FILES['upload'].name
    data, _sep, _rest = str(upload_name).partition('\x00')
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
