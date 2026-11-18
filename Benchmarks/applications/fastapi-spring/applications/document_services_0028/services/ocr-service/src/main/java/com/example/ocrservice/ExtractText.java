// SPDX-License-Identifier: Apache-2.0
package com.example.ocrservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ExtractText {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("documents_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/ExtractText")
    public void extractText(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = inboundPayload.value != null ? inboundPayload.value : "";
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        safeMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = safeMapper.readTree(heading);
        response.getWriter().print(node.path("name").asText());
    }
}
