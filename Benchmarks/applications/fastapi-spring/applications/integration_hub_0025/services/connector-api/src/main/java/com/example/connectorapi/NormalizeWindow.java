// SPDX-License-Identifier: Apache-2.0
package com.example.connectorapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class NormalizeWindow {


    @GetMapping("/NormalizeWindow")
    public void normalizeWindow(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(footnote, "json");
        String handshake = pair.getKey();
        if (!handshake.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + handshake + "</div>");
    }
}
