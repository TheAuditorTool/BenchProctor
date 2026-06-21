// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest55160 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @PostMapping(path="/BenchmarkTest55160", consumes="application/xml")
    public void BenchmarkTest55160(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = expandTabs(xmlValue);
        if (System.currentTimeMillis() > 1000000000000L) {
            try (com.mongodb.client.MongoClient mongoClient = com.mongodb.client.MongoClients.create("mongodb://localhost:27017")) {
                com.mongodb.client.MongoCollection<org.bson.Document> mongoUsers = mongoClient.getDatabase("benchmark").getCollection("users");
                org.bson.Document nosqlResult = mongoUsers.find(new org.bson.Document("username", data)).first();
                response.getWriter().print(nosqlResult != null ? nosqlResult.toJson() : "{}");
            }
        }
    }
}
