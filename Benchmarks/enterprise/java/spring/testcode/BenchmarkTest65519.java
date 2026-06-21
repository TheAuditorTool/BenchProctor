// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest65519 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest65519")
    public void BenchmarkTest65519(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = normalize(refererValue);
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
