# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def enrich_ledger(request):
    snippet = request.FILES['upload'].name
    reader = make_reader(snippet)
    montage = reader()
    requests.get(str(montage))
    return JsonResponse({"saved": True})
