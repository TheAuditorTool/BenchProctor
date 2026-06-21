# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33506(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % (raw_body,)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
