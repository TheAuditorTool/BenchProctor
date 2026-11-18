// SPDX-License-Identifier: Apache-2.0
package com.example.mappingstore;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CollectConnector {


    @GetMapping("/CollectConnector")
    public void collectConnector(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String blurb = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(blurb, "header");
        String handshake = edge.getKey();
        if (!handshake.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + handshake + "</div>");
    }
}
