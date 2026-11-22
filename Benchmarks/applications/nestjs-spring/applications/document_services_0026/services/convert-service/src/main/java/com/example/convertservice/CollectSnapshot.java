// SPDX-License-Identifier: Apache-2.0
package com.example.convertservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CollectSnapshot {


    @GetMapping("/CollectSnapshot")
    public void collectSnapshot(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = xForwardedFor != null ? xForwardedFor : "";
        String addendum = preface.isEmpty() ? "default" : preface;
        if (!addendum.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + addendum + "</div>");
    }
}
