// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class LoadReceipt {


    @GetMapping("/LoadReceipt")
    public void loadReceipt(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(paragraph, "header");
        String bulletin = edge.getKey();
        if (!bulletin.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + bulletin + "</div>");
    }
}
