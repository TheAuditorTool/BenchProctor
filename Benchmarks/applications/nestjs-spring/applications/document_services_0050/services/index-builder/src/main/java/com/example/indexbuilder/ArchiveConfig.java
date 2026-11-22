// SPDX-License-Identifier: Apache-2.0
package com.example.indexbuilder;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class ArchiveConfig {


    @GetMapping("/ArchiveConfig")
    public void archiveConfig(@javax.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = userAgent != null ? userAgent : "";
        String dossier = citation.isEmpty() ? "default" : citation;
        class SchemaInput {
            @javax.validation.constraints.Pattern(regexp = "^[a-zA-Z0-9 _.%\\-]+$") final String value;
            SchemaInput(String value) { this.value = value; }
        }
        javax.validation.Validator schemaValidator = javax.validation.Validation.buildDefaultValidatorFactory().getValidator();
        if (!schemaValidator.validate(new SchemaInput(dossier)).isEmpty()) { response.sendError(400, "schema invalid"); return; }
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + dossier});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
