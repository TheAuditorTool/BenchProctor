// SPDX-License-Identifier: Apache-2.0
package com.example.canarycontroller;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class PromoteCanary {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("delivery_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/PromoteCanary")
    public void promoteCanary(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = inboundPayload.value != null ? inboundPayload.value : "";
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = objectMapper.readValue(subject.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        response.getWriter().print(deserialized);
    }
}
