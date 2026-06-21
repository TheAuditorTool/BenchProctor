// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest44981 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest44981")
    public void BenchmarkTest44981(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = normalize(hostValue);
        response.getWriter().print(data + ",data\n");
    }
}
