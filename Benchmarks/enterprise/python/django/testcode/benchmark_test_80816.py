# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest80816(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
