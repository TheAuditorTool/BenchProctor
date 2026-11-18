// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class EnrichDigest {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/EnrichDigest", consumes="application/json")
    public void enrichDigest(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String inquiry;
        try { inquiry = String.valueOf(Integer.parseInt(note)); }
        catch (NumberFormatException e) { inquiry = note; }
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(inquiry)) { response.sendError(403); return; }
        String grievance = "/var/app/data/" + inquiry;
        Files.write(Paths.get(grievance), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
