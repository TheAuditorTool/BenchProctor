// SPDX-License-Identifier: Apache-2.0
package com.example.screeningservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ReconcileRecord {


    @GetMapping("/ReconcileRecord/{pathId}")
    public void reconcileRecord(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = pathId;
        String grievance = java.net.URLDecoder.decode(subject, java.nio.charset.StandardCharsets.UTF_8);
        String verdict = grievance.matches("^(plain|markdown|html|text)$") ? grievance : "plain";
        response.getWriter().print("<div>" + verdict + "</div>");
    }
}
