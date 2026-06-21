# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest11597(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
