// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest37529 {

    @GetMapping("/BenchmarkTest37529/{pathId}")
    public void BenchmarkTest37529(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        Object evaluated = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(pathValue).getValue();
        response.getWriter().print("<div>" + evaluated + "</div>");
    }
}
