// SPDX-License-Identifier: Apache-2.0
package com.example.customsservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class DeclareCustoms {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("shipping_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/DeclareCustoms")
    public void declareCustoms(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = inboundPayload.value != null ? inboundPayload.value : "";
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(summary)) { response.sendError(403); return; }
        String consignment = "/var/app/data/" + summary;
        Files.delete(Paths.get(consignment));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
