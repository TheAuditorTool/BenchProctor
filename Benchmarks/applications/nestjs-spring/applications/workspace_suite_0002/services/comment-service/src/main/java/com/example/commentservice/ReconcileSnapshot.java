// SPDX-License-Identifier: Apache-2.0
package com.example.commentservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ReconcileSnapshot {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/ReconcileSnapshot", consumes="text/plain")
    public void reconcileSnapshot(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = rawBody != null ? rawBody : "";
        String heading = normalize(transcript);
        if (!heading.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + heading + "</div>");
    }
}
