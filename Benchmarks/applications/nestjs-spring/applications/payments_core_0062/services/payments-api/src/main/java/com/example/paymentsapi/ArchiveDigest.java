// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ArchiveDigest {


    @GetMapping("/ArchiveDigest")
    public void archiveDigest(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = userAgent != null ? userAgent : "";
        String disbursement;
        try { disbursement = String.valueOf(Integer.parseInt(headline)); }
        catch (NumberFormatException e) { disbursement = headline; }
        java.nio.file.Path baseName = java.nio.file.Paths.get(disbursement).getFileName();
        String remittance = "/var/app/data/" + (baseName == null ? "index" : baseName.toString());
        String content = Files.readString(Paths.get(remittance), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
