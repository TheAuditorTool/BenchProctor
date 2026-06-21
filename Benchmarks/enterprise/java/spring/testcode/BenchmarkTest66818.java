// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest66818 {

    @GetMapping("/BenchmarkTest66818")
    public void BenchmarkTest66818(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        response.setContentType("application/json");
        response.getWriter().print("{\"echo\":\"" + refererValue + "\"}");
    }
}
