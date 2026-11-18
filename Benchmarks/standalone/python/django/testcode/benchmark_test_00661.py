# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from pydantic import Field, ValidationError, create_model


def BenchmarkTest00661(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.%\\-]+$")))(value=str(header_value))
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = header_value
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
