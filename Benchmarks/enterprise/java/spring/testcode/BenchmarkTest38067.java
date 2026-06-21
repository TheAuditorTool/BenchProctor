// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest38067 {

    @GetMapping("/BenchmarkTest38067")
    public void BenchmarkTest38067(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        StringBuilder bundle = new StringBuilder();
        bundle.append(authHeader);
        String data = bundle.toString();
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            new Socket(data, 80).close();
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
