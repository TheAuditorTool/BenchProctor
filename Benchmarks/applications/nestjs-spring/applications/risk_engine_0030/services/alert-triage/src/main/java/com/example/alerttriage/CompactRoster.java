// SPDX-License-Identifier: Apache-2.0
package com.example.alerttriage;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactRoster {


    @GetMapping("/CompactRoster/{pathId}")
    public void compactRoster(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = pathId;
        String grievance = java.net.URLDecoder.decode(summary, java.nio.charset.StandardCharsets.UTF_8);
        String verdict = grievance.matches("^(plain|markdown|html|text)$") ? grievance : "plain";
        response.getWriter().print("<div>" + verdict + "</div>");
    }
}
