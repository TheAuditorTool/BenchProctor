// SPDX-License-Identifier: Apache-2.0
package com.example.rateshopper;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class BuildSnapshot {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BuildSnapshot")
    public void buildSnapshot(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = sessionToken != null ? sessionToken : "";
        String parcel = normalize(caption);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(parcel).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String consignment = resolved.toString();
        Files.write(Paths.get(consignment), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
