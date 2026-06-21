// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest64968 {

    private static final java.util.concurrent.atomic.AtomicReference<String> ref = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest64968")
    public void BenchmarkTest64968(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        ref.set(uaValue);
        String data = ref.get();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            try (com.mongodb.client.MongoClient mongoClient = com.mongodb.client.MongoClients.create("mongodb://localhost:27017")) {
                com.mongodb.client.MongoCollection<org.bson.Document> mongoUsers = mongoClient.getDatabase("benchmark").getCollection("users");
                org.bson.Document nosqlResult = mongoUsers.find(new org.bson.Document("username", data)).first();
                response.getWriter().print(nosqlResult != null ? nosqlResult.toJson() : "{}");
            }
        }
    }
}
