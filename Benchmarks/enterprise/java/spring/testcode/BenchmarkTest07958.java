// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest07958 {

    @GetMapping("/BenchmarkTest07958")
    public void BenchmarkTest07958(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + userId;
        String data = valueSupplier.get();
        response.sendError(500, data);
    }
}
