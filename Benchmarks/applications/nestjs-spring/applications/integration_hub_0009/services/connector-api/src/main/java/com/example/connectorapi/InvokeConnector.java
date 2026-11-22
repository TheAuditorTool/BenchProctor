// SPDX-License-Identifier: Apache-2.0
package com.example.connectorapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class InvokeConnector {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("integrations_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/InvokeConnector")
    public void invokeConnector(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String quotation = inboundPayload.value != null ? inboundPayload.value : "";
        response.setContentType("text/html;charset=UTF-8");
        response.getOutputStream().write(("<div class=\"comment\">" + quotation + "</div>").getBytes(java.nio.charset.StandardCharsets.UTF_8));
    }
}
