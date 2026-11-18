// SPDX-License-Identifier: Apache-2.0
package com.example.platformapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.multipart.MultipartFile;

@RestController
class CompactQuota {


    @PostMapping(path="/CompactQuota", consumes="multipart/form-data")
    public void compactQuota(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = file != null ? file.getOriginalFilename() : "";
        String persona;
        try { persona = String.valueOf(Integer.parseInt(tagline)); }
        catch (NumberFormatException e) { persona = tagline; }
        String content = Files.readString(Paths.get("/var/app/data/" + persona), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
