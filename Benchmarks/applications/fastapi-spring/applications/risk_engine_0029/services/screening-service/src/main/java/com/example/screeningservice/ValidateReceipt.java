// SPDX-License-Identifier: Apache-2.0
package com.example.screeningservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.multipart.MultipartFile;

@RestController
class ValidateReceipt {


    @PostMapping(path="/ValidateReceipt", consumes="multipart/form-data")
    public void validateReceipt(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = file != null ? file.getOriginalFilename() : "";
        String grievance;
        try { grievance = String.valueOf(Integer.parseInt(subject)); }
        catch (NumberFormatException e) { grievance = subject; }
        String content = Files.readString(Paths.get("/var/app/data/" + grievance), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
