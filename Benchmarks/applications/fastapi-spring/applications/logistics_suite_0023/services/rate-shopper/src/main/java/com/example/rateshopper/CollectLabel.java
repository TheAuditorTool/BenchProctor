// SPDX-License-Identifier: Apache-2.0
package com.example.rateshopper;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.multipart.MultipartFile;

@RestController
class CollectLabel {


    @PostMapping(path="/CollectLabel", consumes="multipart/form-data")
    public void collectLabel(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = file != null ? file.getOriginalFilename() : "";
        String parcel;
        try { parcel = String.valueOf(Integer.parseInt(caption)); }
        catch (NumberFormatException e) { parcel = caption; }
        String content = Files.readString(Paths.get("/var/app/data/" + parcel), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
