// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15278 {

    @GetMapping("/BenchmarkTest15278/{pathId}")
    public void BenchmarkTest15278(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        if (!pathValue.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        response.setHeader("Refresh", "0; url=" + pathValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
