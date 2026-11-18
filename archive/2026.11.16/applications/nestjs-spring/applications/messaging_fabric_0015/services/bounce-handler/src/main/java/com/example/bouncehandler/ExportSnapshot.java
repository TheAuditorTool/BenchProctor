// SPDX-License-Identifier: Apache-2.0
package com.example.bouncehandler;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ExportSnapshot {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/ExportSnapshot")
    public void exportSnapshot(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = sessionToken != null ? sessionToken : "";
        String bulletin = normalize(heading);
        String excerpt = bulletin.matches("^(status|info|list|show)$") ? bulletin : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + excerpt}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
