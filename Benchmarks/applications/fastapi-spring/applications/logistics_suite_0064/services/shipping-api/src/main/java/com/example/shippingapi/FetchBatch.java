// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class FetchBatch {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/FetchBatch", consumes="application/json")
    public void fetchBatch(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String parcel;
        try { parcel = String.valueOf(Integer.parseInt(transcript)); }
        catch (NumberFormatException e) { parcel = transcript; }
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(parcel)) { response.sendError(403); return; }
        String consignment = "/var/app/data/" + parcel;
        Files.write(Paths.get(consignment), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
