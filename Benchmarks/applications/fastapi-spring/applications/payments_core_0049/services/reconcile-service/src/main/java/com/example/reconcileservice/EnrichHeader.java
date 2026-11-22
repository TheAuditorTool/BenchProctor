// SPDX-License-Identifier: Apache-2.0
package com.example.reconcileservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class EnrichHeader {


    @PostMapping(path="/EnrichHeader", consumes="text/plain")
    public void enrichHeader(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = rawBody != null ? rawBody : "";
        String disbursement = headline.isEmpty() ? "default" : headline;
        String remittance = disbursement.matches("^(status|info|list|show)$") ? disbursement : "status";
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command("/bin/bash", "-c", "ping -c 1 -- " + remittance);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
