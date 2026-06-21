// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15450 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest15450")
    public void BenchmarkTest15450(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = normalize(refererValue);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
