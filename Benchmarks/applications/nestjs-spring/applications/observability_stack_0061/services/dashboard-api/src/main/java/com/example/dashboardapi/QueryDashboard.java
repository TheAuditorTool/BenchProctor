// SPDX-License-Identifier: Apache-2.0
package com.example.dashboardapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class QueryDashboard {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("telemetry_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/QueryDashboard")
    public void queryDashboard(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String quotation = inboundPayload.value != null ? inboundPayload.value : "";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + quotation}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
