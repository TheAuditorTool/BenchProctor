# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest10416(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
