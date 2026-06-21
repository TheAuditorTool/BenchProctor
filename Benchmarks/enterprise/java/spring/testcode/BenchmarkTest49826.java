// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest49826 {

    @GetMapping("/BenchmarkTest49826/{pathId}")
    public void BenchmarkTest49826(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String processed = pathValue.replace("\r", "").replace("\n", "").replaceAll("[A-Za-z0-9]{4,}", "****");
        response.setHeader("X-Forwarded-For", processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
