// SPDX-License-Identifier: Apache-2.0
package com.example.changelogbuilder;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class PublishProfile {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/PublishProfile", consumes="application/json")
    public void publishProfile(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.util.Properties store = new java.util.Properties();
        store.setProperty("value", footnote);
        String wording = store.getProperty("value", "");
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(wording.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        response.getWriter().print(deserialized);
    }
}
