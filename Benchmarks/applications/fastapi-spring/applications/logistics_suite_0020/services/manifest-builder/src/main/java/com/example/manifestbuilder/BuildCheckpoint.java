// SPDX-License-Identifier: Apache-2.0
package com.example.manifestbuilder;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.multipart.MultipartFile;

@RestController
class BuildCheckpoint {


    @PostMapping(path="/BuildCheckpoint", consumes="multipart/form-data")
    public void buildCheckpoint(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = file != null ? file.getOriginalFilename() : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : transcript.split(",")) { tokens.add(token.trim()); }
        String consignment = String.join(",", tokens);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(consignment).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String parcel = resolved.toString();
        String content = Files.readString(Paths.get(parcel), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
