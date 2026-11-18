# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import os
from pydantic import Field, ValidationError, create_model


def BenchmarkTest00298(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = ' '.join(str(env_value).split())
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.%\\-]+$")))(value=str(data))
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
