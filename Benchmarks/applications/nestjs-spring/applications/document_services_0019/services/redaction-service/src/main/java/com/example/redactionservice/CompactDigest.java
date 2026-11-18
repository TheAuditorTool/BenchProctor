// SPDX-License-Identifier: Apache-2.0
package com.example.redactionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class CompactDigest {


    @GetMapping("/CompactDigest")
    public void compactDigest(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String passage = xForwardedFor != null ? xForwardedFor : "";
        String dossier;
        try { dossier = String.valueOf(Integer.parseInt(passage)); }
        catch (NumberFormatException e) { dossier = passage; }
        Files.delete(Paths.get("/var/app/data/" + dossier));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
