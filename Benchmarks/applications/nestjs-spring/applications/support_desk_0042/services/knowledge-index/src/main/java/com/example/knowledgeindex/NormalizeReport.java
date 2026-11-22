// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class NormalizeReport {


    @PostMapping(path="/NormalizeReport", consumes="text/plain")
    public void normalizeReport(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String blurb = rawBody != null ? rawBody : "";
        String inquiry;
        if (blurb.length() > 256) { inquiry = blurb.substring(0, 256); }
        else { inquiry = blurb; }
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(inquiry)) { response.sendError(403); return; }
        String grievance = inquiry;
        Runtime.getRuntime().exec(new String[]{grievance}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
