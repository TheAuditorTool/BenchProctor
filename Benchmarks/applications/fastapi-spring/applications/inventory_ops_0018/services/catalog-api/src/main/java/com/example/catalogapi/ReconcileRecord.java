// SPDX-License-Identifier: Apache-2.0
package com.example.catalogapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ReconcileRecord {


    @GetMapping("/ReconcileRecord")
    public void reconcileRecord(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(transcript, "form");
        String backorder = kv.getKey();
        if (!backorder.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + backorder + "</div>");
    }
}
