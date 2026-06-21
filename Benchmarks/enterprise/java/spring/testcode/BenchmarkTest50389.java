// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest50389 {

    @GetMapping("/BenchmarkTest50389")
    public void BenchmarkTest50389(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = "" + userId;
        if (!data.isEmpty()) throw new IllegalArgumentException("invalid input: " + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
