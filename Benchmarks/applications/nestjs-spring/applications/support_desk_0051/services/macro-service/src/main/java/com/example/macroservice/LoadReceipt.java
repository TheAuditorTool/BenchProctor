// SPDX-License-Identifier: Apache-2.0
package com.example.macroservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class LoadReceipt {


    @GetMapping("/LoadReceipt")
    public void loadReceipt(@javax.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = xForwardedFor != null ? xForwardedFor : "";
        String grievance = preface.isEmpty() ? "default" : preface;
        if (!grievance.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + grievance + "</div>");
    }
}
