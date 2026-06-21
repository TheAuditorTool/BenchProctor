// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest09398 {

    @PostMapping("/BenchmarkTest09398")
    public void BenchmarkTest09398(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        Object evaluated = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(commentValue).getValue();
        response.getWriter().print("<div>" + evaluated + "</div>");
    }
}
