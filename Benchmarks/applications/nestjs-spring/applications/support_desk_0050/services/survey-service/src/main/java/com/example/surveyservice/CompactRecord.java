// SPDX-License-Identifier: Apache-2.0
package com.example.surveyservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import jakarta.validation.Valid;

@RestController
class CompactRecord {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/CompactRecord")
    public void compactRecord(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : remark.split(",")) { tokens.add(token.trim()); }
        String inquiry = String.join(",", tokens);
        java.net.URI parsed = java.net.URI.create(inquiry);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { response.sendError(403); return; }
        String grievance = inquiry;
        String socketRaw = String.valueOf(grievance);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
