// SPDX-License-Identifier: Apache-2.0
package com.example.activityfeed;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class CompactSchedule {


    @PostMapping(path="/CompactSchedule", consumes="text/plain")
    public void compactSchedule(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = rawBody != null ? rawBody : "";
        String wording;
        if (paragraph.length() > 256) { wording = paragraph.substring(0, 256); }
        else { wording = paragraph; }
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(wording)) { response.sendError(403); return; }
        String transcript = wording;
        Runtime.getRuntime().exec(new String[]{transcript}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
