// SPDX-License-Identifier: Apache-2.0
package com.example.captionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FormatAsset {


    @PostMapping(path="/FormatAsset", consumes="text/plain")
    public void formatAsset(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = rawBody != null ? rawBody : "";
        String montage = snippet.isEmpty() ? "default" : snippet;
        String rendition = montage.matches("^(status|info|list|show)$") ? montage : "status";
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command("/bin/bash", "-c", "ping -c 1 -- " + rendition);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
