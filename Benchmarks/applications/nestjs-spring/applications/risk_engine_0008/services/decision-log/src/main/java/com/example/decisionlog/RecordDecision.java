// SPDX-License-Identifier: Apache-2.0
package com.example.decisionlog;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RecordDecision {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("risk_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/RecordDecision")
    public void recordDecision(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = inboundPayload.value != null ? inboundPayload.value : "";
        new ProcessBuilder("echo", excerpt).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
