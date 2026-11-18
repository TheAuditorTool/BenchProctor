// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class SummarizeCheckpoint {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/SummarizeCheckpoint", consumes="text/plain")
    public void summarizeCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = rawBody != null ? rawBody : "";
        String inquiry = normalize(note);
        if (!inquiry.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + inquiry + "</div>");
    }
}
