// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest70860 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest70860")
    public void BenchmarkTest70860(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = normalize(refererValue);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
