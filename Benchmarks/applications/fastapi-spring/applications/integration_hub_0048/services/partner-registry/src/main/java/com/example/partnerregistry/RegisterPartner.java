// SPDX-License-Identifier: Apache-2.0
package com.example.partnerregistry;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RegisterPartner {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("integrations_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/RegisterPartner")
    public void registerPartner(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = inboundPayload.value != null ? inboundPayload.value : "";
        String heading = org.owasp.encoder.Encode.forHtml(preface);
        response.getWriter().print("<div>" + heading + "</div>");
    }
}
