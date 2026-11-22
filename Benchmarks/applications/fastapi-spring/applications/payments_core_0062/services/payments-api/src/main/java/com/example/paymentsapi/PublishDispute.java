// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.multipart.MultipartFile;

@RestController
class PublishDispute {


    @PostMapping(path="/PublishDispute", consumes="multipart/form-data")
    public void publishDispute(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = file != null ? file.getOriginalFilename() : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : headline.split(",")) { tokens.add(token.trim()); }
        String disbursement = String.join(",", tokens);
        Files.delete(Paths.get("/var/app/data/" + disbursement));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
