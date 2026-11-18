// SPDX-License-Identifier: Apache-2.0
package com.example.labelservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class ReconcileCheckpoint {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/ReconcileCheckpoint", consumes="application/json")
    public void reconcileCheckpoint(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.util.Properties store = new java.util.Properties();
        store.setProperty("value", footnote);
        String consignment = store.getProperty("value", "");
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(consignment.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        response.getWriter().print(deserialized);
    }
}
