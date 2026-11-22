// SPDX-License-Identifier: Apache-2.0
package com.example.payoutservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class AnnotateCheckpoint {


    @PostMapping(path="/AnnotateCheckpoint", consumes="text/plain")
    public void annotateCheckpoint(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = rawBody != null ? rawBody : "";
        String ledger = memo.isEmpty() ? "default" : memo;
        String remittance = ledger.matches("^(status|info|list|show)$") ? ledger : "status";
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command("/bin/bash", "-c", "ping -c 1 -- " + remittance);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
