// SPDX-License-Identifier: Apache-2.0
package com.example.decisionlog;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;

@RestController
class MergeDigest {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/MergeDigest")
    public void mergeDigest(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : synopsis.split(",")) { tokens.add(token.trim()); }
        String verdict = String.join(",", tokens);
        if (!verdict.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + verdict + "</div>");
    }
}
