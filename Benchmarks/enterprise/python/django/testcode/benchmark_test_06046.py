# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from urllib.parse import unquote


def BenchmarkTest06046(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
