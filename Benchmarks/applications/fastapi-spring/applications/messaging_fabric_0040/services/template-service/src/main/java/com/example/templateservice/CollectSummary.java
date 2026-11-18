// SPDX-License-Identifier: Apache-2.0
package com.example.templateservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CollectSummary {


    @GetMapping("/CollectSummary")
    public void collectSummary(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(preface, "http");
        String bulletin = pair.getKey();
        if (!bulletin.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + bulletin + "</div>");
    }
}
