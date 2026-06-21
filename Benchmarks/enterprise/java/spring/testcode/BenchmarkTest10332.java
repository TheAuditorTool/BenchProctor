// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest10332 {

    @GetMapping("/BenchmarkTest10332")
    public void BenchmarkTest10332(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.List<String> tokens = java.util.Arrays.asList(userId.split(","));
        String data = String.join(",", tokens);
        int boundedVal;
        try { boundedVal = Integer.parseInt(data); }
        catch (NumberFormatException e) { response.sendError(400); return; }
        if (boundedVal < 0 || boundedVal > 1048576) { response.sendError(400); return; }
        long requested = boundedVal;
        long allocSize = requested + 1;
        response.setHeader("X-Alloc-Size", String.valueOf(allocSize));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
