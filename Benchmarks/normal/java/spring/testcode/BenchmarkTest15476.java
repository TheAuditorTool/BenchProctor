// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15476 {

    private static final java.util.concurrent.atomic.AtomicReference<String> stateBox = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest15476")
    public void BenchmarkTest15476(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        stateBox.set(authHeader);
        String data = stateBox.get();
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            byte[] serBytes = java.util.Base64.getDecoder().decode(data);
            try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
                Object obj = ois.readObject();
                response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
            }
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
