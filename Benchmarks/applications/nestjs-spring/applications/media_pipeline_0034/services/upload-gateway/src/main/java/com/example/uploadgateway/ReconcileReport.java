// SPDX-License-Identifier: Apache-2.0
package com.example.uploadgateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ReconcileReport {


    @GetMapping("/ReconcileReport")
    public void reconcileReport(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = userAgent != null ? userAgent : "";
        String rendition;
        try { rendition = String.valueOf(Integer.parseInt(synopsis)); }
        catch (NumberFormatException e) { rendition = synopsis; }
        java.nio.file.Path baseName = java.nio.file.Paths.get(rendition).getFileName();
        String montage = "/var/app/data/" + (baseName == null ? "index" : baseName.toString());
        String content = Files.readString(Paths.get(montage), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
