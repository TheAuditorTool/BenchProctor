// SPDX-License-Identifier: Apache-2.0
package com.example.redactionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class SummarizeRecord {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/SummarizeRecord", consumes="text/plain")
    public void summarizeRecord(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String passage = rawBody != null ? rawBody : "";
        String dossier = normalize(passage);
        if (!dossier.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + dossier + "</div>");
    }
}
