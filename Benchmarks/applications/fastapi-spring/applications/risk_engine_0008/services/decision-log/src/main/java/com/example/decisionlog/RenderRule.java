// SPDX-License-Identifier: Apache-2.0
package com.example.decisionlog;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.multipart.MultipartFile;

@RestController
class RenderRule {


    @PostMapping(path="/RenderRule", consumes="multipart/form-data")
    public void renderRule(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = file != null ? file.getOriginalFilename() : "";
        String verdict;
        try { verdict = String.valueOf(Integer.parseInt(synopsis)); }
        catch (NumberFormatException e) { verdict = synopsis; }
        String content = Files.readString(Paths.get("/var/app/data/" + verdict), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
