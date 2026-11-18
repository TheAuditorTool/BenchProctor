// SPDX-License-Identifier: Apache-2.0
package com.example.platformapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.multipart.MultipartFile;

@RestController
class CompactFlag {


    @PostMapping(path="/CompactFlag", consumes="multipart/form-data")
    public void compactFlag(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = file != null ? file.getOriginalFilename() : "";
        String handshake;
        if (note.length() > 256) { handshake = note.substring(0, 256); }
        else { handshake = note; }
        String content = Files.readString(Paths.get("/var/app/data/" + handshake), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
