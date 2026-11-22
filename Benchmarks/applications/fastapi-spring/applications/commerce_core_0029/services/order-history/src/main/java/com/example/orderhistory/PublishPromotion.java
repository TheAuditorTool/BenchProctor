// SPDX-License-Identifier: Apache-2.0
package com.example.orderhistory;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.multipart.MultipartFile;

@RestController
class PublishPromotion {


    @PostMapping(path="/PublishPromotion", consumes="multipart/form-data")
    public void publishPromotion(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String notice = file != null ? file.getOriginalFilename() : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : notice.split(",")) { tokens.add(token.trim()); }
        String backorder = String.join(",", tokens);
        Files.delete(Paths.get("/var/app/data/" + backorder));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
