// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest39355 {

    @GetMapping("/BenchmarkTest39355")
    public void BenchmarkTest39355(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = "" + userId;
        if (!data.isEmpty()) throw new Exception("processing error: " + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
