// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest35209 {

    @GetMapping("/BenchmarkTest35209")
    public void BenchmarkTest35209(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = "[%s]".formatted(userId);
        response.sendError(500, data);
    }
}
