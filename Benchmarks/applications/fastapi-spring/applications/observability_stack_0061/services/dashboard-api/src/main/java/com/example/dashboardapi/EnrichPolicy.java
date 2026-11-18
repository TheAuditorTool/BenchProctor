// SPDX-License-Identifier: Apache-2.0
package com.example.dashboardapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.multipart.MultipartFile;

@RestController
class EnrichPolicy {


    @PostMapping(path="/EnrichPolicy", consumes="multipart/form-data")
    public void enrichPolicy(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = file != null ? file.getOriginalFilename() : "";
        String cohort;
        try { cohort = String.valueOf(Integer.parseInt(headline)); }
        catch (NumberFormatException e) { cohort = headline; }
        String content = Files.readString(Paths.get("/var/app/data/" + cohort), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
