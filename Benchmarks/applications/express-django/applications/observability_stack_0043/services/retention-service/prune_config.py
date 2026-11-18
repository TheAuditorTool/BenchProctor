# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def prune_config(request):
    note = request.FILES['upload'].name
    gauge, _sep, _rest = str(note).partition('\x00')
    db.execute('SELECT * FROM "' + str(gauge).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
