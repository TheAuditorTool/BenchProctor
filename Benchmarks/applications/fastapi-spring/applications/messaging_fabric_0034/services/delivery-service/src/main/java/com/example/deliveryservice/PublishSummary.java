// SPDX-License-Identifier: Apache-2.0
package com.example.deliveryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PublishSummary {


    @GetMapping("/PublishSummary")
    public void publishSummary(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = authorization != null ? authorization : "";
        String bulletin;
        try { bulletin = new String(java.util.Base64.getDecoder().decode(footnote), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { bulletin = footnote; }
        String heading = bulletin.matches("^(status|info|list|show)$") ? bulletin : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + heading}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
