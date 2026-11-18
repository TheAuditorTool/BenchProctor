// SPDX-License-Identifier: Apache-2.0
package com.example.mappingstore;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.multipart.MultipartFile;

@RestController
class FetchRecord {


    @PostMapping(path="/FetchRecord", consumes="multipart/form-data")
    public void fetchRecord(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String blurb = file != null ? file.getOriginalFilename() : "";
        String handshake;
        if (blurb.length() > 256) { handshake = blurb.substring(0, 256); }
        else { handshake = blurb; }
        String content = Files.readString(Paths.get("/var/app/data/" + handshake), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
