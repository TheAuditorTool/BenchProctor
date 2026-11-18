// SPDX-License-Identifier: Apache-2.0
package com.example.screeningservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;

@RestController
class CollectWindow {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/CollectWindow")
    public void collectWindow(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : subject.split(",")) { tokens.add(token.trim()); }
        String grievance = String.join(",", tokens);
        if (!grievance.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + grievance + "</div>");
    }
}
