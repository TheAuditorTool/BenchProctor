// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ReconcileRoster {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/ReconcileRoster")
    public void reconcileRoster(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = sessionToken != null ? sessionToken : "";
        String parcel = normalize(transcript);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(parcel).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String consignment = resolved.toString();
        Files.write(Paths.get(consignment), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
