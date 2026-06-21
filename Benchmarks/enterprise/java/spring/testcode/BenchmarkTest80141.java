// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest80141 {

    @GetMapping("/BenchmarkTest80141")
    public void BenchmarkTest80141(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        response.setContentType("text/html");
        response.getWriter().print(originValue);
    }
}
