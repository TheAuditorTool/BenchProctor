// SPDX-License-Identifier: Apache-2.0
package com.example.retryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class NormalizeHeader {


    @GetMapping("/NormalizeHeader")
    public void normalizeHeader(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(synopsis, "query");
        String handshake = edge.getKey();
        if (!handshake.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + handshake + "</div>");
    }
}
