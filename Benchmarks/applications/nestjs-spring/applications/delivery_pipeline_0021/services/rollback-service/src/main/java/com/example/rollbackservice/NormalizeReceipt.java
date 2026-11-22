// SPDX-License-Identifier: Apache-2.0
package com.example.rollbackservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class NormalizeReceipt {


    @GetMapping("/NormalizeReceipt")
    public void normalizeReceipt(@javax.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = userAgent != null ? userAgent : "";
        String phrase;
        try { phrase = String.valueOf(Integer.parseInt(summary)); }
        catch (NumberFormatException e) { phrase = summary; }
        java.nio.file.Path baseName = java.nio.file.Paths.get(phrase).getFileName();
        String subtitle = "/var/app/data/" + (baseName == null ? "index" : baseName.toString());
        String content = Files.readString(Paths.get(subtitle), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
