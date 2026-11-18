// SPDX-License-Identifier: Apache-2.0
package com.example.connectorapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ResolveMapping {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/ResolveMapping", consumes="application/json")
    public void resolveMapping(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String handshake;
        try { handshake = String.valueOf(Integer.parseInt(footnote)); }
        catch (NumberFormatException e) { handshake = footnote; }
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(handshake)) { response.sendError(403); return; }
        String blurb = "/var/app/data/" + handshake;
        Files.write(Paths.get(blurb), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
