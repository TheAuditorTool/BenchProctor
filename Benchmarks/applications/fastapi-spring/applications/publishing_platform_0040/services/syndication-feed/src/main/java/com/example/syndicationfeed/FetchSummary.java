// SPDX-License-Identifier: Apache-2.0
package com.example.syndicationfeed;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class FetchSummary {


    @PostMapping(path="/FetchSummary", consumes="text/plain")
    public void fetchSummary(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = rawBody != null ? rawBody : "";
        byte[] raw = transcript.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String addendum = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        String byline = addendum.matches("^(plain|markdown|html|text)$") ? addendum : "plain";
        response.getWriter().print("<div>" + byline + "</div>");
    }
}
