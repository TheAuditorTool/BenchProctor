// SPDX-License-Identifier: Apache-2.0
package com.example.screeningservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class ResolveSnapshot {


    @GetMapping("/ResolveSnapshot")
    public void resolveSnapshot(@javax.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = xForwardedFor != null ? xForwardedFor : "";
        String verdict = memo.isEmpty() ? "default" : memo;
        if (!verdict.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + verdict + "</div>");
    }
}
