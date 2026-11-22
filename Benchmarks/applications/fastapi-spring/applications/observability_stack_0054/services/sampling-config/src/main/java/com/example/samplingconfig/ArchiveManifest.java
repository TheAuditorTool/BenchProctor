// SPDX-License-Identifier: Apache-2.0
package com.example.samplingconfig;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class ArchiveManifest {


    @GetMapping("/ArchiveManifest")
    public void archiveManifest(@javax.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = userAgent != null ? userAgent : "";
        String prefix = excerpt.length() > 0 ? excerpt.substring(0, 1).toLowerCase() : "";
        String cohort;
        switch (prefix) {
            case "h": cohort = excerpt.toLowerCase(); break;
            case "f": cohort = excerpt.toUpperCase(); break;
            default: cohort = excerpt.strip(); break;
        }
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = objectMapper.readValue(cohort.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        response.getWriter().print(deserialized);
    }
}
