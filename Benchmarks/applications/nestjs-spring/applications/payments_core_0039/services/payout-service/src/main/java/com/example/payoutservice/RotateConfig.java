// SPDX-License-Identifier: Apache-2.0
package com.example.payoutservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class RotateConfig {


    @GetMapping("/RotateConfig")
    public void rotateConfig(@javax.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = userAgent != null ? userAgent : "";
        String ledger;
        try { ledger = String.valueOf(Integer.parseInt(memo)); }
        catch (NumberFormatException e) { ledger = memo; }
        java.nio.file.Path baseName = java.nio.file.Paths.get(ledger).getFileName();
        String remittance = "/var/app/data/" + (baseName == null ? "index" : baseName.toString());
        String content = Files.readString(Paths.get(remittance), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
