// SPDX-License-Identifier: Apache-2.0
package com.example.supplierfeed;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class ReconcileIndex {


    @PostMapping(path="/ReconcileIndex", consumes="text/plain")
    public void reconcileIndex(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = rawBody != null ? rawBody : "";
        String restock = excerpt.isEmpty() ? "default" : excerpt;
        String backorder = restock.matches("^(status|info|list|show)$") ? restock : "status";
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command("/bin/bash", "-c", "ping -c 1 -- " + backorder);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
