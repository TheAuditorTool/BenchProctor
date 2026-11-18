// SPDX-License-Identifier: Apache-2.0
package com.example.fxservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class MergeSnapshot {


    @GetMapping("/MergeSnapshot")
    public void mergeSnapshot(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(headline, "body");
        String disbursement = entry.getKey();
        if (!disbursement.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + disbursement + "</div>");
    }
}
