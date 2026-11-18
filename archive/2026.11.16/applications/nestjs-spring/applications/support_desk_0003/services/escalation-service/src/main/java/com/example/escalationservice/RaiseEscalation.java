// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RaiseEscalation {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("support_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/RaiseEscalation")
    public void raiseEscalation(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = inboundPayload.value != null ? inboundPayload.value : "";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + excerpt});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
