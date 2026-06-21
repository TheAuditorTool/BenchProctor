// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest30378 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @GetMapping("/BenchmarkTest30378")
    public void BenchmarkTest30378(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = toLowerCase(originValue);
        String trustedClaim = data;
        response.setHeader("X-Claim-Trusted", trustedClaim);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
