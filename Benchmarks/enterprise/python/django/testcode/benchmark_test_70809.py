# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70809(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % str(upload_name)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
