// SPDX-License-Identifier: Apache-2.0
package com.example.connectorapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class InvokeConnector {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("integrations_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/InvokeConnector")
    public void invokeConnector(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String passage = inboundPayload.value != null ? inboundPayload.value : "";
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(passage).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String paragraph = resolved.toString();
        Files.write(Paths.get(paragraph), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
