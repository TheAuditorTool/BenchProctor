// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18001 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest18001")
    public void BenchmarkTest18001(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = normalize(hostValue);
        int[] arr = new int[]{10, 20, 30, 40, 50};
        int idx = Integer.parseInt(data);
        response.setHeader("X-Lookup", String.valueOf(arr[idx]));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
