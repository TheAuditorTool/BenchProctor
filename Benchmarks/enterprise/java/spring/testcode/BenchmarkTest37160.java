// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest37160 {

    @GetMapping("/BenchmarkTest37160")
    public void BenchmarkTest37160(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        response.setHeader("Access-Control-Allow-Origin", refererValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
