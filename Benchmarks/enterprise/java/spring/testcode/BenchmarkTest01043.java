// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01043 {

    @PostMapping("/BenchmarkTest01043")
    public void BenchmarkTest01043(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.List<String> tokens = java.util.Arrays.asList(commentValue.split(","));
        String data = String.join(",", tokens);
        String processed = org.owasp.encoder.Encode.forHtml(data);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
