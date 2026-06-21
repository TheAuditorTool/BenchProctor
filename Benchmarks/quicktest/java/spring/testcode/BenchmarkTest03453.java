// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03453 {

    @GetMapping("/BenchmarkTest03453")
    public void BenchmarkTest03453(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = refererValue.isEmpty() ? "default" : refererValue;
        response.sendRedirect(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
