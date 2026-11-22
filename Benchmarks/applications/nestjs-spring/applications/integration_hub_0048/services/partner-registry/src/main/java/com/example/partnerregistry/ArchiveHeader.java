// SPDX-License-Identifier: Apache-2.0
package com.example.partnerregistry;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.validation.Valid;

@RestController
class ArchiveHeader {

    private static class UserInput {
        @javax.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/ArchiveHeader")
    public void archiveHeader(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = req.payload;
        String handshake;
        try { handshake = String.valueOf(Integer.parseInt(citation)); }
        catch (NumberFormatException e) { handshake = citation; }
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        objectMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = objectMapper.readTree(handshake);
        response.getWriter().print(node.path("name").asText());
    }
}
