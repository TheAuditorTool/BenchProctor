// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00111 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping(path="/BenchmarkTest00111", consumes="application/json")
    public void BenchmarkTest00111(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String data;
        if (graphqlVar.length() > 256) { data = graphqlVar.substring(0, 256); }
        else { data = graphqlVar; }
        javax.xml.xpath.XPath xpath = javax.xml.xpath.XPathFactory.newInstance().newXPath();
        Double matchingUsers = xpath.evaluateExpression("count(/users/user[@name='" + data + "'])", new org.xml.sax.InputSource(new java.io.StringReader("<users><user name=\"alice\" role=\"viewer\"/><user name=\"bob\" role=\"admin\"/></users>")), Double.class);
        response.setHeader("X-User-Count", String.valueOf(matchingUsers));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
