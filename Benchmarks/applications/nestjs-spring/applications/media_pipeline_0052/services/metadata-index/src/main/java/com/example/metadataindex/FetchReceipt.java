// SPDX-License-Identifier: Apache-2.0
package com.example.metadataindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;

@RestController
class FetchReceipt {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/FetchReceipt")
    public void fetchReceipt(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : tagline.split(",")) { tokens.add(token.trim()); }
        String rendition = String.join(",", tokens);
        if (!rendition.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + rendition + "</div>");
    }
}
