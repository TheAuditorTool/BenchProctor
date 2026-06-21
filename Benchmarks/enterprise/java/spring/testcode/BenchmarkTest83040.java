// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest83040 {

    @GetMapping("/BenchmarkTest83040")
    public void BenchmarkTest83040(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(userId);
        String data = carrier.toString();
        response.sendError(500, data);
    }
}
