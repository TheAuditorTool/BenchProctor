// SPDX-License-Identifier: Apache-2.0
package com.example.connectorapi;
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
        String heading = file != null ? file.getOriginalFilename() : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : heading.split(",")) { tokens.add(token.trim()); }
        String handshake = String.join(",", tokens);
        Files.delete(Paths.get("/var/app/data/" + handshake));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
