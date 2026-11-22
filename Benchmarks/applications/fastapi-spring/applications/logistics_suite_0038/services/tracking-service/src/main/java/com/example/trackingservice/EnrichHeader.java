// SPDX-License-Identifier: Apache-2.0
package com.example.trackingservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class EnrichHeader {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/EnrichHeader", consumes="application/json")
    public void enrichHeader(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String wording = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : wording.split(",")) { tokens.add(token.trim()); }
        String consignment = String.join(",", tokens);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(consignment).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String parcel = resolved.toString();
        Files.write(Paths.get(parcel), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
