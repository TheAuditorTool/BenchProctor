// SPDX-License-Identifier: Apache-2.0
package com.example.profileapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class UpdateProfile {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("identity_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/UpdateProfile")
    public void updateProfile(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = inboundPayload.value != null ? inboundPayload.value : "";
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        objectMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = objectMapper.readTree(phrase);
        response.getWriter().print(node.path("name").asText());
    }
}
