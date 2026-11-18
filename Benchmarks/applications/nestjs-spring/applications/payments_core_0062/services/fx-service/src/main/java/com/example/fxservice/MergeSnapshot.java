// SPDX-License-Identifier: Apache-2.0
package com.example.fxservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class MergeSnapshot {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/MergeSnapshot", consumes="text/plain")
    public void mergeSnapshot(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = rawBody != null ? rawBody : "";
        String disbursement = normalize(headline);
        if (!disbursement.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + disbursement + "</div>");
    }
}
