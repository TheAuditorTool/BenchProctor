// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest42429 {

    @GetMapping("/BenchmarkTest42429")
    public void BenchmarkTest42429(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(refererValue);
        String data = wrapper.toString();
        if (System.currentTimeMillis() > 1000000000000L) {
            try (com.mongodb.client.MongoClient mongoClient = com.mongodb.client.MongoClients.create("mongodb://localhost:27017")) {
                com.mongodb.client.MongoCollection<org.bson.Document> mongoUsers = mongoClient.getDatabase("benchmark").getCollection("users");
                org.bson.Document nosqlResult = mongoUsers.find(new org.bson.Document("username", data)).first();
                response.getWriter().print(nosqlResult != null ? nosqlResult.toJson() : "{}");
            }
        }
    }
}
