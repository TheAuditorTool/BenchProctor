// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12973 {

    @GetMapping("/BenchmarkTest12973")
    public void BenchmarkTest12973(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = java.net.URLDecoder.decode(userId, "UTF-8");
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        response.getWriter().print(data + ",data\n");
    }
}
