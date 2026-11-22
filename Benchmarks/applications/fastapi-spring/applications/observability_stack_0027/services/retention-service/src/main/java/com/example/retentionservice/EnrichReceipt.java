// SPDX-License-Identifier: Apache-2.0
package com.example.retentionservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.multipart.MultipartFile;

@RestController
class EnrichReceipt {


    @PostMapping(path="/EnrichReceipt", consumes="multipart/form-data")
    public void enrichReceipt(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = file != null ? file.getOriginalFilename() : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : remark.split(",")) { tokens.add(token.trim()); }
        String gauge = String.join(",", tokens);
        Files.delete(Paths.get("/var/app/data/" + gauge));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
