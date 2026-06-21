// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16935 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest16935", consumes="text/plain")
    public void BenchmarkTest16935(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = normalize(rawData);
        try (com.mongodb.client.MongoClient mongoClient = com.mongodb.client.MongoClients.create("mongodb://localhost:27017")) {
            com.mongodb.client.MongoCollection<org.bson.Document> mongoUsers = mongoClient.getDatabase("benchmark").getCollection("users");
            org.bson.Document nosqlResult = mongoUsers.find(new org.bson.Document("username", data)).first();
            response.getWriter().print(nosqlResult != null ? nosqlResult.toJson() : "{}");
        }
    }
}
