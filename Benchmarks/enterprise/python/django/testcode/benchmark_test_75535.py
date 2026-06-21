# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75535(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % (upload_name,)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
