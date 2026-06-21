// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest75890 {

    @GetMapping("/BenchmarkTest75890")
    public void BenchmarkTest75890(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String processed = org.owasp.encoder.Encode.forHtml(envValue);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
