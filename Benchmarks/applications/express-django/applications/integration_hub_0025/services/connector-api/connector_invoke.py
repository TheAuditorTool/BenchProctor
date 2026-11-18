# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import json


@csrf_exempt
def invoke_connector(request):
    headline = json.loads(request.body or b'{}').get("integrations_payload", "")
    os.unlink('/var/app/data/' + str(headline))
    return JsonResponse({"saved": True})
