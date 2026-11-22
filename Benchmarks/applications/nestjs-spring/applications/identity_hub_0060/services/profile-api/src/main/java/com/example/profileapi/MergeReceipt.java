// SPDX-License-Identifier: Apache-2.0
package com.example.profileapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;

@RestController
class MergeReceipt {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/MergeReceipt")
    public void mergeReceipt(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = req.payload;
        String persona;
        try { persona = String.valueOf(Integer.parseInt(paragraph)); }
        catch (NumberFormatException e) { persona = paragraph; }
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        objectMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = objectMapper.readTree(persona);
        response.getWriter().print(node.path("name").asText());
    }
}
