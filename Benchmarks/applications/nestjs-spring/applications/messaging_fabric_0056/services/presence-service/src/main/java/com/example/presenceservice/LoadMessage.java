// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class LoadMessage {


    @PostMapping(path="/LoadMessage", consumes="text/plain")
    public void loadMessage(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = rawBody != null ? rawBody : "";
        String bulletin;
        if (footnote.length() > 256) { bulletin = footnote.substring(0, 256); }
        else { bulletin = footnote; }
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(bulletin)) { response.sendError(403); return; }
        String snippet = bulletin;
        Runtime.getRuntime().exec(new String[]{snippet}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
