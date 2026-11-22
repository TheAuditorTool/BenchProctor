// SPDX-License-Identifier: Apache-2.0
package com.example.captionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class EnrichLedger {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/EnrichLedger")
    public void enrichLedger(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = referer != null ? referer : "";
        String montage = normalize(snippet);
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command("/bin/bash", "-c", "ping -c 1 -- " + montage);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
