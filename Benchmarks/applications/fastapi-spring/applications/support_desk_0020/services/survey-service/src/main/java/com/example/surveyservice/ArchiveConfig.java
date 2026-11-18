// SPDX-License-Identifier: Apache-2.0
package com.example.surveyservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ArchiveConfig {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/ArchiveConfig", consumes="application/json")
    public void archiveConfig(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String inquiry;
        try { inquiry = String.valueOf(Integer.parseInt(phrase)); }
        catch (NumberFormatException e) { inquiry = phrase; }
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(inquiry)) { response.sendError(403); return; }
        String grievance = "/var/app/data/" + inquiry;
        Files.write(Paths.get(grievance), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
