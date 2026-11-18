// SPDX-License-Identifier: Apache-2.0
package com.example.anomalyscorer;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ScoreAnomaly {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("telemetry_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/ScoreAnomaly")
    public void scoreAnomaly(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = inboundPayload.value != null ? inboundPayload.value : "";
        if (!heading.matches("^[a-zA-Z0-9 _.%\\-]+$")) { response.sendError(400); return; }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + heading}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
