// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest72190 {

    @GetMapping("/BenchmarkTest72190")
    public void BenchmarkTest72190(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        response.setHeader("X-Forwarded-For", refererValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
