# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


request_state: dict[str, str] = {}

@csrf_exempt
def publish_invoice(request, path_param):
    caption = request.path.split('/')[-1]
    request_state['last_input'] = caption
    remittance = request_state['last_input']
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(remittance)}))
    return HttpResponse(page)
