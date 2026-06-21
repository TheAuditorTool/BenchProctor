// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest10980 {

    @GetMapping("/BenchmarkTest10980")
    public void BenchmarkTest10980(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        Integer.parseInt(userId);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
