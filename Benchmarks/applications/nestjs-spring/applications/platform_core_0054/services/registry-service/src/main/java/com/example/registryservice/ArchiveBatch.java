// SPDX-License-Identifier: Apache-2.0
package com.example.registryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ArchiveBatch {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/ArchiveBatch", consumes="text/plain")
    public void archiveBatch(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = rawBody != null ? rawBody : "";
        String persona = normalize(snippet);
        if (!persona.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + persona + "</div>");
    }
}
