// SPDX-License-Identifier: Apache-2.0
package com.example.syndicationfeed;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class EnrichSummary {


    @GetMapping("/EnrichSummary")
    public void enrichSummary(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = authorization != null ? authorization : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String byline = transform.apply(synopsis);
        response.getWriter().print("<div>" + byline + "</div>");
    }
}
