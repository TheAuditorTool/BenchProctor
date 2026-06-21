# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest65609(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return JsonResponse({"saved": True})
