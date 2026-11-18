// SPDX-License-Identifier: Apache-2.0
package com.example.bouncehandler;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class VerifyWindow {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/VerifyWindow", consumes="application/json")
    public void verifyWindow(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.util.Properties box = new java.util.Properties();
        box.setProperty("value", summary);
        String bulletin = box.getProperty("value", "");
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(bulletin.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        response.getWriter().print(deserialized);
    }
}
