// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12546 {

    @GetMapping("/BenchmarkTest12546")
    public void BenchmarkTest12546(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        request.getSession().setAttribute("data", String.valueOf(refererValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
