# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest63220(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = '%s' % (json_value,)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
