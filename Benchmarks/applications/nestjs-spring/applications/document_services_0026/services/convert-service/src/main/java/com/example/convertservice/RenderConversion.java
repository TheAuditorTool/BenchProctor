// SPDX-License-Identifier: Apache-2.0
package com.example.convertservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class RenderConversion {


    @GetMapping("/RenderConversion")
    public void renderConversion(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = userAgent != null ? userAgent : "";
        String addendum;
        try { addendum = String.valueOf(Integer.parseInt(preface)); }
        catch (NumberFormatException e) { addendum = preface; }
        java.nio.file.Path baseName = java.nio.file.Paths.get(addendum).getFileName();
        String dossier = "/var/app/data/" + (baseName == null ? "index" : baseName.toString());
        String content = Files.readString(Paths.get(dossier), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
