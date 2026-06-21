// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest38808 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest38808")
    public void BenchmarkTest38808(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = normalize(refererValue);
        response.getWriter().print(data + ",data\n");
    }
}
