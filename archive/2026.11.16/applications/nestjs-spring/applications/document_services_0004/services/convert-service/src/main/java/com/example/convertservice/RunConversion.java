// SPDX-License-Identifier: Apache-2.0
package com.example.convertservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class RunConversion {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("documents_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/RunConversion")
    public void runConversion(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = inboundPayload.value != null ? inboundPayload.value : "";
        Files.delete(Paths.get("/var/app/data/" + headline));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
