// SPDX-License-Identifier: Apache-2.0
package com.example.assetlibrary;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class FetchReceipt {


    @PostMapping(path="/FetchReceipt", consumes="text/plain")
    public void fetchReceipt(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = rawBody != null ? rawBody : "";
        String byline;
        if (note.length() > 256) { byline = note.substring(0, 256); }
        else { byline = note; }
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(byline)) { response.sendError(403); return; }
        String addendum = byline;
        Runtime.getRuntime().exec(new String[]{addendum}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
