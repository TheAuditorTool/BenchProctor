// SPDX-License-Identifier: Apache-2.0
package com.example.alerttriage;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ArchiveSchedule {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/ArchiveSchedule", consumes="application/json")
    public void archiveSchedule(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String grievance;
        try { grievance = String.valueOf(Integer.parseInt(summary)); }
        catch (NumberFormatException e) { grievance = summary; }
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(grievance)) { response.sendError(403); return; }
        String verdict = "/var/app/data/" + grievance;
        Files.write(Paths.get(verdict), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
