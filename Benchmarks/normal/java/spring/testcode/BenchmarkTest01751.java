// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01751 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @GetMapping("/BenchmarkTest01751")
    public void BenchmarkTest01751(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = stripCRLF(originValue);
        if (!data.matches("^[\\w\\s.,;:_/\\-=]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        int[] arr = new int[]{10, 20, 30, 40, 50};
        int idx = Integer.parseInt(data);
        response.setHeader("X-Lookup", String.valueOf(arr[idx]));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
