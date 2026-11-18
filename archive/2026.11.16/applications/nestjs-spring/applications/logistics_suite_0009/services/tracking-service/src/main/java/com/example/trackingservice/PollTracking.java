// SPDX-License-Identifier: Apache-2.0
package com.example.trackingservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class PollTracking {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("shipping_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/PollTracking")
    public void pollTracking(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = inboundPayload.value != null ? inboundPayload.value : "";
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(excerpt).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String consignment = resolved.toString();
        Files.write(Paths.get(consignment), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
