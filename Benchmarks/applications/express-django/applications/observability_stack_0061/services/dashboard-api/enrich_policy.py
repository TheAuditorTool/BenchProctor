# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import socket


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def enrich_policy(request):
    headline = request.body.decode('utf-8')
    reader = make_reader(headline)
    cohort = reader()
    s = socket.create_connection((str(cohort), 80))
    s.close()
    return JsonResponse({"saved": True})
