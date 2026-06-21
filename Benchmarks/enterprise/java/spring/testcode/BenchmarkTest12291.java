// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12291 {

    @GetMapping("/BenchmarkTest12291")
    public void BenchmarkTest12291(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = "[%s]".formatted(authHeader);
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        response.getWriter().print(data + ",data\n");
    }
}
