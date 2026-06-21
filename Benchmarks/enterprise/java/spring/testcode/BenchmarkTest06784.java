// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest06784 {

    @PostMapping("/BenchmarkTest06784")
    public void BenchmarkTest06784(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String processed = org.owasp.encoder.Encode.forHtml(commentValue);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
