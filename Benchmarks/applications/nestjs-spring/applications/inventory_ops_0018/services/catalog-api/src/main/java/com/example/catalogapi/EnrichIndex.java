// SPDX-License-Identifier: Apache-2.0
package com.example.catalogapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;

@RestController
class EnrichIndex {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/EnrichIndex")
    public void enrichIndex(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : transcript.split(",")) { tokens.add(token.trim()); }
        String backorder = String.join(",", tokens);
        if (!backorder.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + backorder + "</div>");
    }
}
