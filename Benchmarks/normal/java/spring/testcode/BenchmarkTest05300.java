// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05300 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest05300")
    public void BenchmarkTest05300(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = normalize(uaValue);
        response.getWriter().print(String.valueOf(data));
    }
}
