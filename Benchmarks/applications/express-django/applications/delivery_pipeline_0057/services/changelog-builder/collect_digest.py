# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def collect_digest(request):
    footnote = request.FILES['upload'].name
    wording, _sep, _rest = str(footnote).partition('\x00')
    db.execute('SELECT * FROM "' + str(wording).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
