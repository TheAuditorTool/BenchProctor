// SPDX-License-Identifier: Apache-2.0
package com.example.metadataindex;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class FetchProfile {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/FetchProfile")
    public void fetchProfile(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = referer != null ? referer : "";
        String rendition = normalize(citation);
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command("/bin/bash", "-c", "ping -c 1 -- " + rendition);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
