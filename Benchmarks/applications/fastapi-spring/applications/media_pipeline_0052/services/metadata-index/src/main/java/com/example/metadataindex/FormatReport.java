// SPDX-License-Identifier: Apache-2.0
package com.example.metadataindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FormatReport {


    @GetMapping("/FormatReport")
    public void formatReport(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = authorization != null ? authorization : "";
        String rendition;
        try { rendition = new String(java.util.Base64.getDecoder().decode(tagline), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { rendition = tagline; }
        String montage = rendition.matches("^(status|info|list|show)$") ? rendition : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + montage}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
