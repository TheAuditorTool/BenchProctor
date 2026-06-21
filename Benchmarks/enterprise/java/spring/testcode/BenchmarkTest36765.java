// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest36765 {

    @GetMapping("/BenchmarkTest36765/{pathId}")
    public void BenchmarkTest36765(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + pathValue;
        String data = valueSupplier.get();
        String escaped = "\"" + data.replace("\"", "\"\"") + "\"";
        response.getWriter().print(escaped + ",data");
    }
}
