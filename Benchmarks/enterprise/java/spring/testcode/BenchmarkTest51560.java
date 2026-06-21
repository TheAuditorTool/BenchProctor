// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest51560 {

    @PostMapping("/BenchmarkTest51560")
    public void BenchmarkTest51560(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + commentValue;
        String data = valueSupplier.get();
        response.sendError(500, data);
    }
}
