// SPDX-License-Identifier: Apache-2.0
package com.example.samplingconfig;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class CollectCheckpoint {


    @PostMapping(path="/CollectCheckpoint", consumes="text/plain")
    public void collectCheckpoint(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = rawBody != null ? rawBody : "";
        String gauge;
        if (paragraph.length() > 256) { gauge = paragraph.substring(0, 256); }
        else { gauge = paragraph; }
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(gauge)) { response.sendError(403); return; }
        String cohort = gauge;
        Runtime.getRuntime().exec(new String[]{cohort}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
