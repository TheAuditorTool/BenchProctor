// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest70141 {

    @PostMapping(path="/BenchmarkTest70141", consumes="application/xml")
    public void BenchmarkTest70141(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        Object evaluated = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(xmlValue).getValue();
        response.getWriter().print("<div>" + evaluated + "</div>");
    }
}
