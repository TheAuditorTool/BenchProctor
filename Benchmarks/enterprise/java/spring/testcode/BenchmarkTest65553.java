// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest65553 {

    @GetMapping("/BenchmarkTest65553")
    public void BenchmarkTest65553(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        try {
            Integer.parseInt(uaValue);
        } catch (Exception e) { }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
