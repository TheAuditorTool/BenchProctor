// SPDX-License-Identifier: Apache-2.0
package com.example.transcodeservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.multipart.MultipartFile;

@RestController
class EnrichThreshold {


    @PostMapping(path="/EnrichThreshold", consumes="multipart/form-data")
    public void enrichThreshold(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String notice = file != null ? file.getOriginalFilename() : "";
        String rendition;
        try { rendition = String.valueOf(Integer.parseInt(notice)); }
        catch (NumberFormatException e) { rendition = notice; }
        String content = Files.readString(Paths.get("/var/app/data/" + rendition), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
