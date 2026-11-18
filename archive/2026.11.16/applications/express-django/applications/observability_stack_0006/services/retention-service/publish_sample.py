# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
import base64
from django.utils.safestring import mark_safe
from django.http import HttpResponse


@csrf_exempt
def publish_sample(request):
    preface = request.META.get('HTTP_AUTHORIZATION', '')
    cohort = base64.b64decode(preface).decode('utf-8', 'ignore')
    return HttpResponse(mark_safe('<div>' + str(cohort) + '</div>'))
