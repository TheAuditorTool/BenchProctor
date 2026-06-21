// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00778 {

    private enum AllowedValue { PLAIN, MARKDOWN, HTML, TEXT }

    @PostMapping(path="/BenchmarkTest00778", consumes="application/xml")
    public void BenchmarkTest00778(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(xmlValue, "form");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        Object evaluated = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data).getValue();
        response.getWriter().print("<div>" + evaluated + "</div>");
    }
}
