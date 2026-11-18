// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RotateRoster {


    @GetMapping("/RotateRoster")
    public void rotateRoster(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(note, "http");
        String inquiry = entry.getKey();
        if (!inquiry.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + inquiry + "</div>");
    }
}
