// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest49401 {

    @GetMapping("/BenchmarkTest49401")
    public void BenchmarkTest49401(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        int divisor = Integer.parseInt(refererValue);
        if (divisor == 0) { response.sendError(400); return; }
        int result = 100 / divisor;
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
