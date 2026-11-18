# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json


@csrf_exempt
def request_return(request):
    transcript = json.loads(request.body or b'{}').get("orders_payload", "")
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", transcript):
        return JsonResponse({'error': 'forbidden'}, status=400)
    voucher = transcript
    with open('/var/app/data/' + str(voucher), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
