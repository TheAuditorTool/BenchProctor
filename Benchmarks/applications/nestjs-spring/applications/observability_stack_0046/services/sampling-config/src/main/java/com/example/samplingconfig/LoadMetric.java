// SPDX-License-Identifier: Apache-2.0
package com.example.samplingconfig;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class LoadMetric {


    @GetMapping("/LoadMetric")
    public void loadMetric(@javax.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = userAgent != null ? userAgent : "";
        String gauge;
        try { gauge = String.valueOf(Integer.parseInt(paragraph)); }
        catch (NumberFormatException e) { gauge = paragraph; }
        java.nio.file.Path baseName = java.nio.file.Paths.get(gauge).getFileName();
        String cohort = "/var/app/data/" + (baseName == null ? "index" : baseName.toString());
        String content = Files.readString(Paths.get(cohort), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
