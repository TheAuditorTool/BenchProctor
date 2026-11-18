// SPDX-License-Identifier: Apache-2.0
package com.example.decisionlog;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class MergeRoster {


    @GetMapping("/MergeRoster")
    public void mergeRoster(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = sessionToken != null ? sessionToken : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : synopsis.split(",")) { tokens.add(token.trim()); }
        String verdict = String.join(",", tokens);
        record SchemaInput(@jakarta.validation.constraints.Pattern(regexp = "^[a-zA-Z0-9 _.%\\-]+$") String value) {}
        jakarta.validation.Validator schemaValidator = jakarta.validation.Validation.buildDefaultValidatorFactory().getValidator();
        if (!schemaValidator.validate(new SchemaInput(verdict)).isEmpty()) { response.sendError(400, "schema invalid"); return; }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + verdict}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
