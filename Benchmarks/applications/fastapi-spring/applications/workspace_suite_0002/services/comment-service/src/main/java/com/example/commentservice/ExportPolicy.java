// SPDX-License-Identifier: Apache-2.0
package com.example.commentservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ExportPolicy {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/ExportPolicy", consumes="application/json")
    public void exportPolicy(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String heading;
        try { heading = String.valueOf(Integer.parseInt(transcript)); }
        catch (NumberFormatException e) { heading = transcript; }
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(heading)) { response.sendError(403); return; }
        String passage = "/var/app/data/" + heading;
        Files.write(Paths.get(passage), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
