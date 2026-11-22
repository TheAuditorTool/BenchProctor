# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def summarize_manifest(request):
    remark = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    gauge = normalize(remark)
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(gauge)}))
    return HttpResponse(page)
