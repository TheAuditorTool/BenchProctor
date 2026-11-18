// SPDX-License-Identifier: Apache-2.0
package com.example.customsservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

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
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(summary.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        response.getWriter().print(deserialized);
    }
}
