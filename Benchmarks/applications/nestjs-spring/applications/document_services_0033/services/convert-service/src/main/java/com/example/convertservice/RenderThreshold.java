// SPDX-License-Identifier: Apache-2.0
package com.example.convertservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RenderThreshold {


    @PostMapping(path="/RenderThreshold", consumes="text/plain")
    public void renderThreshold(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = rawBody != null ? rawBody : "";
        String addendum;
        if (snippet.length() > 256) { addendum = snippet.substring(0, 256); }
        else { addendum = snippet; }
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(addendum)) { response.sendError(403); return; }
        String dossier = addendum;
        Runtime.getRuntime().exec(new String[]{dossier}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
