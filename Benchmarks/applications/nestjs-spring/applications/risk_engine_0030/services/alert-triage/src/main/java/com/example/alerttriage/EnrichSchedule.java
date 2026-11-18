// SPDX-License-Identifier: Apache-2.0
package com.example.alerttriage;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class EnrichSchedule {


    @GetMapping("/EnrichSchedule")
    public void enrichSchedule(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = referer != null ? referer : "";
        String grievance = summary.isEmpty() ? "default" : summary;
        String content = Files.readString(Paths.get("/var/app/data/" + grievance), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
