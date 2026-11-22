// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class PublishReport {


    @PostMapping(path="/PublishReport", consumes="text/plain")
    public void publishReport(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = rawBody != null ? rawBody : "";
        String consignment;
        if (citation.length() > 256) { consignment = citation.substring(0, 256); }
        else { consignment = citation; }
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(consignment)) { response.sendError(403); return; }
        String parcel = consignment;
        Runtime.getRuntime().exec(new String[]{parcel}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
