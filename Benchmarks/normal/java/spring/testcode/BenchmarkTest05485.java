// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05485 {

    @GetMapping("/BenchmarkTest05485")
    public void BenchmarkTest05485(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String normalized = java.text.Normalizer.normalize(refererValue, java.text.Normalizer.Form.NFKC);
        response.setContentType("text/html");
        response.getWriter().print("<p>" + normalized + "</p>");
    }
}
