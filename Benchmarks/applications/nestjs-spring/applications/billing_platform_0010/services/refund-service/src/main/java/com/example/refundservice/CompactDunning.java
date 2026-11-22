// SPDX-License-Identifier: Apache-2.0
package com.example.refundservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class CompactDunning {


    @GetMapping("/CompactDunning")
    public void compactDunning(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = userAgent != null ? userAgent : "";
        String remittance;
        try { remittance = String.valueOf(Integer.parseInt(headline)); }
        catch (NumberFormatException e) { remittance = headline; }
        java.nio.file.Path baseName = java.nio.file.Paths.get(remittance).getFileName();
        String dunning = "/var/app/data/" + (baseName == null ? "index" : baseName.toString());
        String content = Files.readString(Paths.get(dunning), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
