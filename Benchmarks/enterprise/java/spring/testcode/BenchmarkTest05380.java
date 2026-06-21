// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05380 {

    @GetMapping("/BenchmarkTest05380")
    public void BenchmarkTest05380(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        response.getWriter().print("{\"resource\":\"" + refererValue + "\"}");
    }
}
