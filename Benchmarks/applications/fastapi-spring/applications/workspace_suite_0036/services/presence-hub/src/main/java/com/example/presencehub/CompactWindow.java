// SPDX-License-Identifier: Apache-2.0
package com.example.presencehub;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactWindow {


    @GetMapping("/CompactWindow")
    public void compactWindow(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = authorization != null ? authorization : "";
        String synopsis;
        try { synopsis = new String(java.util.Base64.getDecoder().decode(remark), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { synopsis = remark; }
        String quotation = synopsis.matches("^(status|info|list|show)$") ? synopsis : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + quotation}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
