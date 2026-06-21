// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest28663 {

    @GetMapping("/BenchmarkTest28663/{pathId}")
    public void BenchmarkTest28663(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(pathValue, "request");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        response.getWriter().print(data + ",data\n");
    }
}
