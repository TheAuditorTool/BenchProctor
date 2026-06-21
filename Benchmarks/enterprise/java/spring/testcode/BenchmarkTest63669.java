// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest63669 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest63669/{pathId}")
    public void BenchmarkTest63669(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = normalize(pathValue);
        String trustedClaim = data;
        response.setHeader("X-Claim-Trusted", trustedClaim);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
