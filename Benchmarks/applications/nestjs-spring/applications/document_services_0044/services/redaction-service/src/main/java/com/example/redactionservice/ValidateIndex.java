// SPDX-License-Identifier: Apache-2.0
package com.example.redactionservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class ValidateIndex {


    @GetMapping("/ValidateIndex")
    public void validateIndex(@javax.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = xForwardedFor != null ? xForwardedFor : "";
        String dossier = phrase.isEmpty() ? "default" : phrase;
        if (!dossier.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + dossier + "</div>");
    }
}
