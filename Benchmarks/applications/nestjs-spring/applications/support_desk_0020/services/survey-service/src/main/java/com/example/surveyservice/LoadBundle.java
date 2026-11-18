// SPDX-License-Identifier: Apache-2.0
package com.example.surveyservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class LoadBundle {


    @GetMapping("/LoadBundle")
    public void loadBundle(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = referer != null ? referer : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String inquiry = transform.apply(phrase);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(inquiry).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String grievance = resolved.toString();
        Files.write(Paths.get(grievance), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
