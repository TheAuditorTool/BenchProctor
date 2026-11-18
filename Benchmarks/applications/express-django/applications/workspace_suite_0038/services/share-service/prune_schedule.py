# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def prune_schedule(request):
    preface = request.FILES['upload'].name
    remark, _sep, _rest = str(preface).partition('\x00')
    db.execute('SELECT * FROM "' + str(remark).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
