// SPDX-License-Identifier: Apache-2.0
package com.example.platformapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ProvisionTenant {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("platform_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/ProvisionTenant")
    public void provisionTenant(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String quotation = inboundPayload.value != null ? inboundPayload.value : "";
        String persona = quotation.matches("^(config|data|index|schema)$") ? quotation : "config";
        Files.delete(Paths.get("/var/app/data/" + persona));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
