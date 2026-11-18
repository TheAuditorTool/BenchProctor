// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ValidateCheckpoint {


    @GetMapping("/ValidateCheckpoint")
    public void validateCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = referer != null ? referer : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String grievance = transform.apply(summary);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(grievance).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String inquiry = resolved.toString();
        Files.write(Paths.get(inquiry), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
