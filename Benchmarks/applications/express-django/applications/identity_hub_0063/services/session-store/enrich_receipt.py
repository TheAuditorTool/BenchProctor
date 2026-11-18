# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def enrich_receipt(request):
    paragraph = request.FILES['upload'].name
    persona, _sep, _rest = str(paragraph).partition('\x00')
    db.execute('SELECT * FROM "' + str(persona).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
