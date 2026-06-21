// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest71684 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest71684")
    public void BenchmarkTest71684(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = normalize(fieldValue);
        Object evaluated = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data).getValue();
        response.getWriter().print("<div>" + evaluated + "</div>");
    }
}
