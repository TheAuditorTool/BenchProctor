// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest49829 {

    @GetMapping("/BenchmarkTest49829")
    public void BenchmarkTest49829(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        new java.io.File(uaValue).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
