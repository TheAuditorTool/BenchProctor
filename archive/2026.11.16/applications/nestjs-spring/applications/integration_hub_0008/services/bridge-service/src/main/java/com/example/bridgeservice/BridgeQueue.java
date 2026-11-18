// SPDX-License-Identifier: Apache-2.0
package com.example.bridgeservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class BridgeQueue {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("integrations_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/BridgeQueue")
    public void bridgeQueue(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String notice = inboundPayload.value != null ? inboundPayload.value : "";
        String paragraph = org.owasp.encoder.Encode.forHtml(notice);
        response.getWriter().print("<div>" + paragraph + "</div>");
    }
}
