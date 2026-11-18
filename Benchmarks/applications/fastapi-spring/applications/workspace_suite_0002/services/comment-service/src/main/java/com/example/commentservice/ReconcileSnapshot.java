// SPDX-License-Identifier: Apache-2.0
package com.example.commentservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ReconcileSnapshot {


    @GetMapping("/ReconcileSnapshot")
    public void reconcileSnapshot(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(transcript, "form");
        String heading = entry.getKey();
        if (!heading.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + heading + "</div>");
    }
}
