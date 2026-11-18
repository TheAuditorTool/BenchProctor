// SPDX-License-Identifier: Apache-2.0
package com.example.connectorapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ReconcileSnapshot {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/ReconcileSnapshot", consumes="application/json")
    public void reconcileSnapshot(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String handshake;
        try { handshake = String.valueOf(Integer.parseInt(snippet)); }
        catch (NumberFormatException e) { handshake = snippet; }
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(handshake)) { response.sendError(403); return; }
        String paragraph = "/var/app/data/" + handshake;
        Files.write(Paths.get(paragraph), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
