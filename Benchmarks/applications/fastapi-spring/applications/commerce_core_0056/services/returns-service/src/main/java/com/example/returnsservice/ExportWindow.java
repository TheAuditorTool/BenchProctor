// SPDX-License-Identifier: Apache-2.0
package com.example.returnsservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ExportWindow {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/ExportWindow")
    public void exportWindow(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = sessionToken != null ? sessionToken : "";
        String backorder = normalize(citation);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(backorder).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String voucher = resolved.toString();
        Files.write(Paths.get(voucher), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
