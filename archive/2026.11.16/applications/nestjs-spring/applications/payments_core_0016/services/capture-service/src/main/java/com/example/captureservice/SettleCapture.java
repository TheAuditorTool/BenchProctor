// SPDX-License-Identifier: Apache-2.0
package com.example.captureservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class SettleCapture {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("payments_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/SettleCapture")
    public void settleCapture(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String ledger = inboundPayload.value != null ? inboundPayload.value : "";
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        safeMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = safeMapper.readTree(ledger);
        response.getWriter().print(node.path("name").asText());
    }
}
