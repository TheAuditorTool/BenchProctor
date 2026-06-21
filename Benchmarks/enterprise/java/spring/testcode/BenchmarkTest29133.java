// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest29133 {

    @GetMapping("/BenchmarkTest29133")
    public void BenchmarkTest29133(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        if (!userId.isEmpty()) throw new Exception("processing error: " + userId);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
