// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ExportBundle {


    @PostMapping(path="/ExportBundle", consumes="text/plain")
    public void exportBundle(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = rawBody != null ? rawBody : "";
        String bulletin;
        try { bulletin = new String(java.util.Base64.getDecoder().decode(subject), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { bulletin = subject; }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + bulletin}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
