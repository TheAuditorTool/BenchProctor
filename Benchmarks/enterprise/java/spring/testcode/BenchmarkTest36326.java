// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest36326 {

    @PostMapping(path="/BenchmarkTest36326", consumes="application/xml")
    public void BenchmarkTest36326(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.List<String> tokens = java.util.Arrays.asList(xmlValue.split(","));
        String data = String.join(",", tokens);
        int[] arr = new int[]{10, 20, 30, 40, 50};
        int idx = Integer.parseInt(data);
        response.setHeader("X-Lookup", String.valueOf(arr[idx]));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
