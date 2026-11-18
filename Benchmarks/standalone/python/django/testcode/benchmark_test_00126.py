# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from pydantic import Field, ValidationError, create_model


def BenchmarkTest00126(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.%\\-]+$")))(value=str(data))
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
