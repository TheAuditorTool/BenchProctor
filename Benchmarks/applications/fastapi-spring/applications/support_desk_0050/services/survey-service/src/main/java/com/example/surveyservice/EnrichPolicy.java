// SPDX-License-Identifier: Apache-2.0
package com.example.surveyservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class EnrichPolicy {


    @GetMapping("/EnrichPolicy")
    public void enrichPolicy(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = xForwardedFor != null ? xForwardedFor : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : remark.split(",")) { tokens.add(token.trim()); }
        String inquiry = String.join(",", tokens);
        response.getWriter().print("<div>" + inquiry + "</div>");
    }
}
