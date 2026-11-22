// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class RaiseEscalation {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("support_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/RaiseEscalation")
    public void raiseEscalation(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String quotation = inboundPayload.value != null ? inboundPayload.value : "";
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String inquiry = policy.sanitize(quotation);
        response.setContentType("text/html;charset=UTF-8");
        response.getOutputStream().write(("<div class=\"comment\">" + inquiry + "</div>").getBytes(java.nio.charset.StandardCharsets.UTF_8));
    }
}
