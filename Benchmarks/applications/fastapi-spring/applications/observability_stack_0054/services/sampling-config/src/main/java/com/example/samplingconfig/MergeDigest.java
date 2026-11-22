// SPDX-License-Identifier: Apache-2.0
package com.example.samplingconfig;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class MergeDigest {


    @PostMapping(path="/MergeDigest", consumes="text/plain")
    public void mergeDigest(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = rawBody != null ? rawBody : "";
        String cohort = excerpt.isEmpty() ? "default" : excerpt;
        String gauge = cohort.matches("^(status|info|list|show)$") ? cohort : "status";
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command("/bin/bash", "-c", "ping -c 1 -- " + gauge);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
