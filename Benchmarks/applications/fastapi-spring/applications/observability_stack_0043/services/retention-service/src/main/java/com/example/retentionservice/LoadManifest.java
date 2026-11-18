// SPDX-License-Identifier: Apache-2.0
package com.example.retentionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class LoadManifest {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/LoadManifest", consumes="application/json")
    public void loadManifest(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String gauge;
        try { gauge = String.valueOf(Integer.parseInt(note)); }
        catch (NumberFormatException e) { gauge = note; }
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(gauge)) { response.sendError(403); return; }
        String cohort = "/var/app/data/" + gauge;
        Files.write(Paths.get(cohort), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
