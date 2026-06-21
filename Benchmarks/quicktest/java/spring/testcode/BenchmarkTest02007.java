// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02007 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest02007")
    public void BenchmarkTest02007(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = normalize(uaValue);
        response.getWriter().print(String.valueOf(data));
    }
}
