// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15031 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    private enum AllowedValue { PLAIN, MARKDOWN, HTML, TEXT }

    @PostMapping(path="/BenchmarkTest15031", consumes="application/json")
    public void BenchmarkTest15031(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        try { AllowedValue.valueOf(graphqlVar.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { graphqlVar = AllowedValue.values()[0].name().toLowerCase(); }
        Object evaluated = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(graphqlVar).getValue();
        response.getWriter().print("<div>" + evaluated + "</div>");
    }
}
