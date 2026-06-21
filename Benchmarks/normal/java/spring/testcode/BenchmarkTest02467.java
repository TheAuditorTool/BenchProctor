// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02467 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest02467")
    public void BenchmarkTest02467(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = normalize(fieldValue);
        try (com.mongodb.client.MongoClient mongoClient = com.mongodb.client.MongoClients.create("mongodb://localhost:27017")) {
            com.mongodb.client.MongoCollection<org.bson.Document> mongoUsers = mongoClient.getDatabase("benchmark").getCollection("users");
            org.bson.Document nosqlResult = mongoUsers.find(new org.bson.Document("username", data)).first();
            response.getWriter().print(nosqlResult != null ? nosqlResult.toJson() : "{}");
        }
    }
}
