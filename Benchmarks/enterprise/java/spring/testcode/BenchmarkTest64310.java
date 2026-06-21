// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest64310 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest64310", consumes="application/xml")
    public void BenchmarkTest64310(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = normalize(xmlValue);
        Object evaluated = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data).getValue();
        response.getWriter().print("<div>" + evaluated + "</div>");
    }
}
