// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00047 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping("/BenchmarkTest00047")
    public void BenchmarkTest00047(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = String.join(" ", commentValue.split("[ \\t]+"));
        record SchemaInput(@jakarta.validation.constraints.Pattern(regexp = "^[a-zA-Z0-9 _.%~\\-]+$") String value) {}
        jakarta.validation.Validator schemaValidator = jakarta.validation.Validation.buildDefaultValidatorFactory().getValidator();
        if (!schemaValidator.validate(new SchemaInput(data)).isEmpty()) { response.sendError(400, "schema invalid"); return; }
        javax.xml.xpath.XPath xpath = javax.xml.xpath.XPathFactory.newInstance().newXPath();
        javax.xml.xpath.XPathExpression roleQuery = xpath.compile("/users/user[@name='" + data + "']/@role");
        String userRole = roleQuery.evaluate(new org.xml.sax.InputSource(new java.io.StringReader("<users><user name=\"alice\" role=\"viewer\"/><user name=\"bob\" role=\"admin\"/></users>")));
        response.setHeader("X-User-Role", userRole);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
