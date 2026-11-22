// SPDX-License-Identifier: Apache-2.0
package com.example.samplingconfig;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class RenderSchedule {


    @PostMapping(path="/RenderSchedule", consumes="text/plain")
    public void renderSchedule(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = rawBody != null ? rawBody : "";
        String gauge = paragraph.isEmpty() ? "default" : paragraph;
        String cohort = gauge.matches("^(status|info|list|show)$") ? gauge : "status";
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command("/bin/bash", "-c", "ping -c 1 -- " + cohort);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
