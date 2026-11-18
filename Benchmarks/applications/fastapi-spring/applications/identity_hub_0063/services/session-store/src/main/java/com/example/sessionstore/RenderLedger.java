// SPDX-License-Identifier: Apache-2.0
package com.example.sessionstore;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RenderLedger {


    @GetMapping("/RenderLedger")
    public void renderLedger(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = authorization != null ? authorization : "";
        String persona;
        try { persona = new String(java.util.Base64.getDecoder().decode(paragraph), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { persona = paragraph; }
        String synopsis = persona.matches("^(status|info|list|show)$") ? persona : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + synopsis}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
