// SPDX-License-Identifier: Apache-2.0
package com.example.ledgersync;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ResolveSnapshot {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/ResolveSnapshot", consumes="application/json")
    public void resolveSnapshot(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String arrears;
        try { arrears = String.valueOf(Integer.parseInt(synopsis)); }
        catch (NumberFormatException e) { arrears = synopsis; }
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(arrears)) { response.sendError(403); return; }
        String dunning = "/var/app/data/" + arrears;
        Files.write(Paths.get(dunning), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
