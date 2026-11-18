// SPDX-License-Identifier: Apache-2.0
package com.example.thumbnailservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;

@RestController
class AnnotateCaption {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/AnnotateCaption")
    public void annotateCaption(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String passage = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : passage.split(",")) { tokens.add(token.trim()); }
        String montage = String.join(",", tokens);
        if (!montage.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + montage + "</div>");
    }
}
