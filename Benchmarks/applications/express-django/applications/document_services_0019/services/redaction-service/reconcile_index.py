# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def reconcile_index(request):
    passage = request.FILES['upload'].name
    dossier, _sep, _rest = str(passage).partition('\x00')
    db.execute('SELECT * FROM "' + str(dossier).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
