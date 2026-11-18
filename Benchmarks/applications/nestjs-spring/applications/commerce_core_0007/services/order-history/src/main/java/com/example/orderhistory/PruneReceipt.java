// SPDX-License-Identifier: Apache-2.0
package com.example.orderhistory;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;

@RestController
class PruneReceipt {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/PruneReceipt")
    public void pruneReceipt(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : heading.split(",")) { tokens.add(token.trim()); }
        String voucher = String.join(",", tokens);
        if (!voucher.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + voucher + "</div>");
    }
}
