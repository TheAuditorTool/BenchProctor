# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
from urllib.parse import unquote


def BenchmarkTest72642(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
