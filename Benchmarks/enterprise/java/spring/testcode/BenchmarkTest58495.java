// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest58495 {

    @GetMapping("/BenchmarkTest58495")
    public void BenchmarkTest58495(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        if (!refererValue.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        int[] arr = new int[]{10, 20, 30, 40, 50};
        int idx = Integer.parseInt(refererValue);
        response.setHeader("X-Lookup", String.valueOf(arr[idx]));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
