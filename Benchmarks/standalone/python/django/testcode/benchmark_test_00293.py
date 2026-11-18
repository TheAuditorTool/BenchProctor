# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import json
from pydantic import Field, ValidationError, create_model


def BenchmarkTest00293(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = json_value if json_value else 'default'
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.%\\-]+$")))(value=str(data))
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
