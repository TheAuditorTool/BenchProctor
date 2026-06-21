// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest80758 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest80758/{pathId}")
    public void BenchmarkTest80758(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = trimEnds(pathValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        int requested = Integer.parseInt(processed);
        int allocSize = requested + 1;
        response.setHeader("X-Alloc-Size", String.valueOf(allocSize));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
