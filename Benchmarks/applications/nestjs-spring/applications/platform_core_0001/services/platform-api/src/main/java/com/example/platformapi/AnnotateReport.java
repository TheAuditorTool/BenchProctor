// SPDX-License-Identifier: Apache-2.0
package com.example.platformapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AnnotateReport {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/AnnotateReport", consumes="text/plain")
    public void annotateReport(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = rawBody != null ? rawBody : "";
        String persona = normalize(tagline);
        if (!persona.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + persona + "</div>");
    }
}
