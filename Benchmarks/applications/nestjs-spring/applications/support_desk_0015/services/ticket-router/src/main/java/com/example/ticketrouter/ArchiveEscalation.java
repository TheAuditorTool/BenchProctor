// SPDX-License-Identifier: Apache-2.0
package com.example.ticketrouter;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class ArchiveEscalation {


    @GetMapping("/ArchiveEscalation")
    public void archiveEscalation(@javax.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = xForwardedFor != null ? xForwardedFor : "";
        String grievance = phrase.isEmpty() ? "default" : phrase;
        if (!grievance.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + grievance + "</div>");
    }
}
