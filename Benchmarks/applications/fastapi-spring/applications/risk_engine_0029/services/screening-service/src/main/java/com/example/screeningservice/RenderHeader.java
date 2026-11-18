// SPDX-License-Identifier: Apache-2.0
package com.example.screeningservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RenderHeader {


    @GetMapping("/RenderHeader")
    public void renderHeader(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = authorization != null ? authorization : "";
        String grievance;
        try { grievance = new String(java.util.Base64.getDecoder().decode(subject), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { grievance = subject; }
        String verdict = grievance.matches("^(status|info|list|show)$") ? grievance : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + verdict}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
