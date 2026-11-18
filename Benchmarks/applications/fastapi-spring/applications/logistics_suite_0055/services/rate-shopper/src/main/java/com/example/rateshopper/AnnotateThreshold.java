// SPDX-License-Identifier: Apache-2.0
package com.example.rateshopper;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class AnnotateThreshold {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/AnnotateThreshold")
    public void annotateThreshold(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = sessionToken != null ? sessionToken : "";
        String consignment = normalize(heading);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(consignment).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String parcel = resolved.toString();
        Files.write(Paths.get(parcel), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
