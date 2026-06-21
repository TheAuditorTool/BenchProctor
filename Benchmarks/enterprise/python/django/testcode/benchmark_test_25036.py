# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25036(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % str(upload_name)
    exec(str(data))
    return JsonResponse({"saved": True})
