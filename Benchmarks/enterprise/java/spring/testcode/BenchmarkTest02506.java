// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02506 {

    @GetMapping("/BenchmarkTest02506/{pathId}")
    public void BenchmarkTest02506(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("\\s+", " ");
        String data = transform.apply(pathValue);
        Object evaluated = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data).getValue();
        response.getWriter().print("<div>" + evaluated + "</div>");
    }
}
