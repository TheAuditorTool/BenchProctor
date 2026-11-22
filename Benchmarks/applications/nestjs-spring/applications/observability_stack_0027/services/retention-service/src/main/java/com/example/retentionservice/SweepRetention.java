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
        String headline = inboundPayload.value != null ? inboundPayload.value : "";
        org.apache.hc.client5.http.classic.methods.HttpGet fetchRequest = new org.apache.hc.client5.http.classic.methods.HttpGet(headline);
        try (org.apache.hc.client5.http.impl.classic.CloseableHttpClient fetchClient = org.apache.hc.client5.http.impl.classic.HttpClients.createDefault()) {
            int fetchStatus = fetchClient.execute(fetchRequest, fetchResponse -> fetchResponse.getCode());
            response.setHeader("X-Fetch-Status", String.valueOf(fetchStatus));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
