// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest66341 {

    @GetMapping("/BenchmarkTest66341")
    public void BenchmarkTest66341(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(userId, "cookie");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        response.sendError(500, data);
    }
}
