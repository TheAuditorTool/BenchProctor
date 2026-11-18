// SPDX-License-Identifier: Apache-2.0
package com.example.alerttriage;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class TriageAlert {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("risk_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/TriageAlert")
    public void triageAlert(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = inboundPayload.value != null ? inboundPayload.value : "";
        String verdict = headline.matches("^(status|info|list|show)$") ? headline : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + verdict}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
