// SPDX-License-Identifier: Apache-2.0
package com.example.syndicationfeed;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class SummarizeConfig {


    @PostMapping(path="/SummarizeConfig", consumes="text/plain")
    public void summarizeConfig(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = rawBody != null ? rawBody : "";
        String addendum;
        if (transcript.length() > 256) { addendum = transcript.substring(0, 256); }
        else { addendum = transcript; }
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(addendum)) { response.sendError(403); return; }
        String byline = addendum;
        Runtime.getRuntime().exec(new String[]{byline}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
