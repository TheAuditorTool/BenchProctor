# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def prune_report(request):
    remark = request.FILES['upload'].name
    remittance, _sep, _rest = str(remark).partition('\x00')
    db.execute('SELECT * FROM "' + str(remittance).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
