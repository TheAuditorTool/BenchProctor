// SPDX-License-Identifier: Apache-2.0
package com.example.returnsservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RotateWindow {


    @GetMapping("/RotateWindow")
    public void rotateWindow(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = authorization != null ? authorization : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : citation.split(",")) { tokens.add(token.trim()); }
        String backorder = String.join(",", tokens);
        new ProcessBuilder("echo", backorder).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
