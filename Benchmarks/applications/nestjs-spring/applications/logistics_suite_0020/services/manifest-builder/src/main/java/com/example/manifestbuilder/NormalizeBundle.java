// SPDX-License-Identifier: Apache-2.0
package com.example.manifestbuilder;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class NormalizeBundle {


    @PostMapping(path="/NormalizeBundle", consumes="text/plain")
    public void normalizeBundle(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = rawBody != null ? rawBody : "";
        String consignment;
        if (transcript.length() > 256) { consignment = transcript.substring(0, 256); }
        else { consignment = transcript; }
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(consignment)) { response.sendError(403); return; }
        String parcel = consignment;
        Runtime.getRuntime().exec(new String[]{parcel}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
