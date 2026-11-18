// SPDX-License-Identifier: Apache-2.0
package com.example.retentionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class PruneConfig {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/PruneConfig", consumes="application/json")
    public void pruneConfig(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.util.Properties box = new java.util.Properties();
        box.setProperty("value", note);
        String gauge = box.getProperty("value", "");
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(gauge.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        response.getWriter().print(deserialized);
    }
}
