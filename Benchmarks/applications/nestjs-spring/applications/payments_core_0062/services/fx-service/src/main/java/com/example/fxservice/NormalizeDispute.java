// SPDX-License-Identifier: Apache-2.0
package com.example.fxservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;

@RestController
class NormalizeDispute {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/NormalizeDispute")
    public void normalizeDispute(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : headline.split(",")) { tokens.add(token.trim()); }
        String disbursement = String.join(",", tokens);
        if (!disbursement.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + disbursement + "</div>");
    }
}
