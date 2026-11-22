// SPDX-License-Identifier: Apache-2.0
package com.example.convertservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.multipart.MultipartFile;

@RestController
class BuildRoster {


    @PostMapping(path="/BuildRoster", consumes="multipart/form-data")
    public void buildRoster(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = file != null ? file.getOriginalFilename() : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : footnote.split(",")) { tokens.add(token.trim()); }
        String addendum = String.join(",", tokens);
        Files.delete(Paths.get("/var/app/data/" + addendum));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
