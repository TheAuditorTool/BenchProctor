// SPDX-License-Identifier: Apache-2.0
package com.example.platformapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ExportWindow {


    @GetMapping("/ExportWindow")
    public void exportWindow(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = authorization != null ? authorization : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : excerpt.split(",")) { tokens.add(token.trim()); }
        String handshake = String.join(",", tokens);
        new ProcessBuilder("echo", handshake).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
