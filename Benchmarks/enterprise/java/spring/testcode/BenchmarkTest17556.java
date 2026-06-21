// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17556 {

    @GetMapping("/BenchmarkTest17556/{pathId}")
    public void BenchmarkTest17556(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        if (!("true".equals(pathValue) || "false".equals(pathValue))) { response.sendError(400); return; }
        System.setProperty("app.user.preference", pathValue);
        response.setHeader("X-Config-Set", "app.user.preference");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
