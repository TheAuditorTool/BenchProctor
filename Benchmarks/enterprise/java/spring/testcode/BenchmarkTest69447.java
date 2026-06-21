// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest69447 {

    @GetMapping("/BenchmarkTest69447")
    public void BenchmarkTest69447(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        Integer.parseInt(userId);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
