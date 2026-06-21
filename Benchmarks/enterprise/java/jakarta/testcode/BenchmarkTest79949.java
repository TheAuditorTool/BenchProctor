// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest79949 {

    @POST
    @Path("/BenchmarkTest79949")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest79949(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = String.format("%s", fieldValue);
        try (com.mongodb.client.MongoClient mongoClient = com.mongodb.client.MongoClients.create("mongodb://localhost:27017")) {
            com.mongodb.client.MongoCollection<org.bson.Document> mongoUsers = mongoClient.getDatabase("benchmark").getCollection("users");
            org.bson.Document nosqlResult = mongoUsers.find(new org.bson.Document("username", data)).first();
            return Response.ok(nosqlResult != null ? nosqlResult.toJson() : "{}", MediaType.TEXT_HTML).build();
        }
    }
}
