# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11191(request):
    upload_name = request.FILES['doc'].name
    data = '%s' % (upload_name,)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
