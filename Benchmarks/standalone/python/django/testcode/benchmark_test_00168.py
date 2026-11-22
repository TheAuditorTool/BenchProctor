# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from pathlib import Path


def BenchmarkTest00168(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = '%s' % (env_value,)
    Path('/var/app/data/' + str(data)).write_text('data')
    return JsonResponse({"saved": True})
