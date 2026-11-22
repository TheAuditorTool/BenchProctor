// SPDX-License-Identifier: Apache-2.0
package com.example.watchlistsync;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class FetchBundle {


    @GetMapping("/FetchBundle")
    public void fetchBundle(@javax.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = xForwardedFor != null ? xForwardedFor : "";
        String verdict = excerpt.isEmpty() ? "default" : excerpt;
        if (!verdict.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + verdict + "</div>");
    }
}
