// SPDX-License-Identifier: Apache-2.0
package com.example.platformapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ExportManifest {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/ExportManifest", consumes="application/json")
    public void exportManifest(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String persona;
        try { persona = String.valueOf(Integer.parseInt(tagline)); }
        catch (NumberFormatException e) { persona = tagline; }
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(persona)) { response.sendError(403); return; }
        String handshake = "/var/app/data/" + persona;
        Files.write(Paths.get(handshake), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
