// SPDX-License-Identifier: Apache-2.0
package com.example.redactionservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class ApplyRedaction {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("documents_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/ApplyRedaction")
    public void applyRedaction(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = inboundPayload.value != null ? inboundPayload.value : "";
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command("/bin/bash", "-c", "ping -c 1 -- " + synopsis);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
