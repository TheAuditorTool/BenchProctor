// SPDX-License-Identifier: Apache-2.0
package com.example.alertrouter;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RotateCheckpoint {


    @GetMapping("/RotateCheckpoint")
    public void rotateCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = authorization != null ? authorization : "";
        String gauge;
        try { gauge = new String(java.util.Base64.getDecoder().decode(excerpt), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { gauge = excerpt; }
        String cohort = gauge.matches("^(status|info|list|show)$") ? gauge : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + cohort}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
