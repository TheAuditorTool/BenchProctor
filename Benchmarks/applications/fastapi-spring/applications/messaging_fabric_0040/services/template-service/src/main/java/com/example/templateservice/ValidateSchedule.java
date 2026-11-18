// SPDX-License-Identifier: Apache-2.0
package com.example.templateservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ValidateSchedule {


    @GetMapping("/ValidateSchedule")
    public void validateSchedule(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = authorization != null ? authorization : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : preface.split(",")) { tokens.add(token.trim()); }
        String bulletin = String.join(",", tokens);
        new ProcessBuilder("echo", bulletin).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
