// SPDX-License-Identifier: Apache-2.0
package com.example.retentionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class SweepRetention {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("telemetry_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/SweepRetention")
    public void sweepRetention(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = inboundPayload.value != null ? inboundPayload.value : "";
        response.getWriter().print("<div>" + excerpt + "</div>");
    }
}
