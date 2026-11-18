// SPDX-License-Identifier: Apache-2.0
package com.example.registryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CollectReceipt {


    @GetMapping("/CollectReceipt")
    public void collectReceipt(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(snippet, "body");
        String persona = edge.getKey();
        if (!persona.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + persona + "</div>");
    }
}
