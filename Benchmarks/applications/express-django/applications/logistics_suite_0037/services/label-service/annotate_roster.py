# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def annotate_roster(request):
    footnote = request.FILES['upload'].name
    consignment, _sep, _rest = str(footnote).partition('\x00')
    db.execute('SELECT * FROM "' + str(consignment).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
