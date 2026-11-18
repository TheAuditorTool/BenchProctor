// SPDX-License-Identifier: Apache-2.0
package com.example.connectorapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class EnrichCheckpoint {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/EnrichCheckpoint", consumes="text/plain")
    public void enrichCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = rawBody != null ? rawBody : "";
        String handshake = normalize(footnote);
        if (!handshake.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + handshake + "</div>");
    }
}
