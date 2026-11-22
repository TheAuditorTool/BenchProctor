// SPDX-License-Identifier: Apache-2.0
package com.example.logshipper;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class LoadRecord {


    @GetMapping("/LoadRecord")
    public void loadRecord(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = host != null ? host : "";
        String cohort = note.isEmpty() ? "default" : note;
        String gauge = cohort.matches("^(config|data|index|schema)$") ? cohort : "config";
        Files.write(Paths.get("/var/uploads/" + gauge), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
