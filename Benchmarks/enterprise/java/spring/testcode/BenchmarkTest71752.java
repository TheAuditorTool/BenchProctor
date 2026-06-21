// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest71752 {

    private enum AllowedValue { ACTIVE, PENDING, DELETED, ARCHIVED }

    @GetMapping("/BenchmarkTest71752")
    public void BenchmarkTest71752(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        try { AllowedValue.valueOf(hostValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { hostValue = AllowedValue.values()[0].name().toLowerCase(); }
        try (com.mongodb.client.MongoClient mongoClient = com.mongodb.client.MongoClients.create("mongodb://localhost:27017")) {
            com.mongodb.client.MongoCollection<org.bson.Document> mongoUsers = mongoClient.getDatabase("benchmark").getCollection("users");
            org.bson.Document nosqlResult = mongoUsers.find(new org.bson.Document("username", hostValue)).first();
            response.getWriter().print(nosqlResult != null ? nosqlResult.toJson() : "{}");
        }
    }
}
