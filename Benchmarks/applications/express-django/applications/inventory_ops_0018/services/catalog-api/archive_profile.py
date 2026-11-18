# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import socket


@csrf_exempt
def archive_profile(request):
    transcript = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    backorder = normalize(transcript)
    s = socket.create_connection((str(backorder), 80))
    s.close()
    return JsonResponse({"saved": True})
