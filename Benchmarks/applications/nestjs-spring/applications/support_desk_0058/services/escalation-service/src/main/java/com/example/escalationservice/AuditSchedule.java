// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class AuditSchedule {


    @PostMapping(path="/AuditSchedule", consumes="text/plain")
    public void auditSchedule(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = rawBody != null ? rawBody : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String inquiry = transform.apply(snippet);
        if (!inquiry.matches("^[a-zA-Z0-9 _.#~\\-]+$")) { response.sendError(400); return; }
        Files.write(Paths.get("/var/uploads/" + inquiry), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
