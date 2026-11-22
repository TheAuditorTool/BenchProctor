// SPDX-License-Identifier: Apache-2.0
package com.example.quotaservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.multipart.MultipartFile;

@RestController
class ArchiveSummary {


    @PostMapping(path="/ArchiveSummary", consumes="multipart/form-data")
    public void archiveSummary(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = file != null ? file.getOriginalFilename() : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : remark.split(",")) { tokens.add(token.trim()); }
        String persona = String.join(",", tokens);
        Files.delete(Paths.get("/var/app/data/" + persona));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
