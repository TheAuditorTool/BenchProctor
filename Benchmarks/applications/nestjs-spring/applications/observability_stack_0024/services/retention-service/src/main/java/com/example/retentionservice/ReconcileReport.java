// SPDX-License-Identifier: Apache-2.0
package com.example.retentionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;

@RestController
class ReconcileReport {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/ReconcileReport")
    public void reconcileReport(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : summary.split(",")) { tokens.add(token.trim()); }
        String cohort = String.join(",", tokens);
        if (!cohort.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + cohort + "</div>");
    }
}
