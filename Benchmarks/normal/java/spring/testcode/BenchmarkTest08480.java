// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08480 {

    @PostMapping("/BenchmarkTest08480")
    public void BenchmarkTest08480(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(commentValue, "http");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        response.getWriter().print(data + ",data\n");
    }
}
