// SPDX-License-Identifier: Apache-2.0
package com.example.metadataindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class FormatPolicy {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/FormatPolicy")
    public void formatPolicy(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = sessionToken != null ? sessionToken : "";
        String rendition = normalize(tagline);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(rendition).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String montage = resolved.toString();
        Files.write(Paths.get(montage), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
