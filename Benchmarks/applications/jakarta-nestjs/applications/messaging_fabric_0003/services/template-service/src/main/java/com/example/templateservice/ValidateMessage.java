// SPDX-License-Identifier: Apache-2.0
package com.example.templateservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class ValidateMessage {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @POST
    @Path("/ValidateMessage/graphql")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response validateMessage(GraphQLRequest req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String subject = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.util.Properties box = new java.util.Properties();
        box.setProperty("value", subject);
        String bulletin = box.getProperty("value", "");
        String passage = bulletin.matches("^(config|data|index|schema)$") ? bulletin : "config";
        String content = Files.readString(Paths.get("/var/app/data/" + passage), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
