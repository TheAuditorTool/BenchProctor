// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest37566 {

    @PostMapping(path="/BenchmarkTest37566", consumes="text/plain")
    public void BenchmarkTest37566(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        if (!rawData.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        int[] arr = new int[]{10, 20, 30, 40, 50};
        int idx = Integer.parseInt(rawData);
        response.setHeader("X-Lookup", String.valueOf(arr[idx]));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
