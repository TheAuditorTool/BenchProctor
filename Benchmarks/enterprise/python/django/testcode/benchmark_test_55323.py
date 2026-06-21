# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest55323(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
