// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class EnrichBatch {


    @GetMapping("/EnrichBatch")
    public void enrichBatch(@javax.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = userAgent != null ? userAgent : "";
        String grievance;
        try { grievance = String.valueOf(Integer.parseInt(preface)); }
        catch (NumberFormatException e) { grievance = preface; }
        java.nio.file.Path baseName = java.nio.file.Paths.get(grievance).getFileName();
        String inquiry = "/var/app/data/" + (baseName == null ? "index" : baseName.toString());
        String content = Files.readString(Paths.get(inquiry), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
