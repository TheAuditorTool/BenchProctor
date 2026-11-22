// SPDX-License-Identifier: Apache-2.0
package com.example.ticketrouter;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class SummarizeConfig {


    @GetMapping("/SummarizeConfig")
    public void summarizeConfig(@javax.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = userAgent != null ? userAgent : "";
        String grievance = phrase.isEmpty() ? "default" : phrase;
        class SchemaInput {
            @javax.validation.constraints.Pattern(regexp = "^[a-zA-Z0-9 _.%\\-]+$") final String value;
            SchemaInput(String value) { this.value = value; }
        }
        javax.validation.Validator schemaValidator = javax.validation.Validation.buildDefaultValidatorFactory().getValidator();
        if (!schemaValidator.validate(new SchemaInput(grievance)).isEmpty()) { response.sendError(400, "schema invalid"); return; }
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + grievance});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
