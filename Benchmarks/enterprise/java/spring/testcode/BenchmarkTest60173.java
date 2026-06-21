// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60173 {

    @PostMapping("/BenchmarkTest60173")
    public void BenchmarkTest60173(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        if (!fieldValue.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        try (com.mongodb.client.MongoClient mongoClient = com.mongodb.client.MongoClients.create("mongodb://localhost:27017")) {
            com.mongodb.client.MongoCollection<org.bson.Document> mongoUsers = mongoClient.getDatabase("benchmark").getCollection("users");
            org.bson.Document nosqlResult = mongoUsers.find(new org.bson.Document("username", fieldValue)).first();
            response.getWriter().print(nosqlResult != null ? nosqlResult.toJson() : "{}");
        }
    }
}
