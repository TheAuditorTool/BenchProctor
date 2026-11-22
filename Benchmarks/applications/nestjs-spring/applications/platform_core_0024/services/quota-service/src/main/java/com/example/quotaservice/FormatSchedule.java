// SPDX-License-Identifier: Apache-2.0
package com.example.quotaservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FormatSchedule {


    @GetMapping("/FormatSchedule")
    public void formatSchedule(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = xForwardedFor != null ? xForwardedFor : "";
        String handshake = heading.isEmpty() ? "default" : heading;
        if (!handshake.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + handshake + "</div>");
    }
}
