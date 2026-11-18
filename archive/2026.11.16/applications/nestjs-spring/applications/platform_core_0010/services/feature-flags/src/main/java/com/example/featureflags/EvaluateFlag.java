// SPDX-License-Identifier: Apache-2.0
package com.example.featureflags;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class EvaluateFlag {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("platform_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/EvaluateFlag")
    public void evaluateFlag(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = inboundPayload.value != null ? inboundPayload.value : "";
        String handshake = synopsis.matches("^(status|info|list|show)$") ? synopsis : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + handshake}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
