// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest52420 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest52420")
    public void BenchmarkTest52420(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = trimEnds(refererValue);
        if (System.currentTimeMillis() > 1000000000000L) {
            response.getWriter().print("<div>" + data + "</div>");
        }
    }
}
