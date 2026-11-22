# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def publish_receipt(request, path_param):
    memo = request.path.split('/')[-1]
    ledger = f'{memo!s}'
    os.unlink('/var/app/data/' + str(ledger))
    return JsonResponse({"saved": True})
