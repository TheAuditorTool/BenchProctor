// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest79270 {

    @GetMapping("/BenchmarkTest79270")
    public void BenchmarkTest79270(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = String.format("%s", authHeader);
        String processed = org.owasp.encoder.Encode.forHtml(data);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
