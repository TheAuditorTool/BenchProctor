// SPDX-License-Identifier: Apache-2.0
package com.example.mappingstore;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import jakarta.validation.Valid;

@RestController
class FetchLedger {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/FetchLedger")
    public void fetchLedger(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String blurb = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : blurb.split(",")) { tokens.add(token.trim()); }
        String handshake = String.join(",", tokens);
        java.net.URI parsed = java.net.URI.create(handshake);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { response.sendError(403); return; }
        String citation = handshake;
        String socketRaw = String.valueOf(citation);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
