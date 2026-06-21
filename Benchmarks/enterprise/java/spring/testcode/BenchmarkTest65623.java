// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest65623 {

    @GetMapping("/BenchmarkTest65623/{pathId}")
    public void BenchmarkTest65623(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        if ("admin".equals(pathValue)) {
            response.getWriter().print("{\"role\":\"admin\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
