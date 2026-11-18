// SPDX-License-Identifier: Apache-2.0
package com.example.labelservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ValidateProfile {


    @GetMapping("/ValidateProfile")
    public void validateProfile(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = xForwardedFor != null ? xForwardedFor : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : footnote.split(",")) { tokens.add(token.trim()); }
        String consignment = String.join(",", tokens);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(consignment).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String parcel = resolved.toString();
        Files.write(Paths.get(parcel), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
