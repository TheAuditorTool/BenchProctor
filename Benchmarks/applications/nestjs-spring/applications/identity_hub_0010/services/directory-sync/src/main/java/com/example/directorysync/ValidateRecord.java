// SPDX-License-Identifier: Apache-2.0
package com.example.directorysync;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;

@RestController
class ValidateRecord {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/ValidateRecord")
    public void validateRecord(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : phrase.split(",")) { tokens.add(token.trim()); }
        String persona = String.join(",", tokens);
        if (!persona.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + persona + "</div>");
    }
}
