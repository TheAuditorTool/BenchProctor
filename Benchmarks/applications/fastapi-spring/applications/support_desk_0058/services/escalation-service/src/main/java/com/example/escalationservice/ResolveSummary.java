// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class ResolveSummary {


    @PostMapping("/ResolveSummary")
    public void resolveSummary(@javax.validation.constraints.Size(max = 4096) @RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = field != null ? field : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(snippet, "form");
        String inquiry = kv.getKey();
        String grievance = inquiry.matches("^(status|info|list|show)$") ? inquiry : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + grievance});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
