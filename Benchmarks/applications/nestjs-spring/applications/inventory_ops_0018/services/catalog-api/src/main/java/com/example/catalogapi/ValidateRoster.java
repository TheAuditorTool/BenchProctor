// SPDX-License-Identifier: Apache-2.0
package com.example.catalogapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import jakarta.validation.Valid;

@RestController
class ValidateRoster {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/ValidateRoster")
    public void validateRoster(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : transcript.split(",")) { tokens.add(token.trim()); }
        String backorder = String.join(",", tokens);
        java.net.URI parsed = java.net.URI.create(backorder);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { response.sendError(403); return; }
        String restock = backorder;
        String socketRaw = String.valueOf(restock);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
