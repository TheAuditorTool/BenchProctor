// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18656 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest18656")
    public void BenchmarkTest18656(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = normalize(uaValue);
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
