# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import socket


@csrf_exempt
def fetch_ledger(request):
    passage = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    montage = normalize(passage)
    s = socket.create_connection((str(montage), 80))
    s.close()
    return JsonResponse({"saved": True})
