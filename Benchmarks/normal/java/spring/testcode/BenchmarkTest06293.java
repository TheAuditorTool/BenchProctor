// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest06293 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @GetMapping("/BenchmarkTest06293")
    public void BenchmarkTest06293(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = stripCRLF(originValue);
        String trustedClaim = data;
        response.setHeader("X-Claim-Trusted", trustedClaim);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
