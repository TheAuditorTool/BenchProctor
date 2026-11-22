// SPDX-License-Identifier: Apache-2.0
package com.example.watchlistsync;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ReconcileCheckpoint {


    @GetMapping("/ReconcileCheckpoint")
    public void reconcileCheckpoint(@javax.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = userAgent != null ? userAgent : "";
        String verdict;
        try { verdict = String.valueOf(Integer.parseInt(excerpt)); }
        catch (NumberFormatException e) { verdict = excerpt; }
        java.nio.file.Path baseName = java.nio.file.Paths.get(verdict).getFileName();
        String grievance = "/var/app/data/" + (baseName == null ? "index" : baseName.toString());
        String content = Files.readString(Paths.get(grievance), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
