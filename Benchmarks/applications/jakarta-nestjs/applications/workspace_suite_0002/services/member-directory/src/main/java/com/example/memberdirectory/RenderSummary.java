// SPDX-License-Identifier: Apache-2.0
package com.example.memberdirectory;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class RenderSummary {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @POST
    @Path("/RenderSummary/graphql")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response renderSummary(GraphQLRequest req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String transcript = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.util.Properties store = new java.util.Properties();
        store.setProperty("value", transcript);
        String heading = store.getProperty("value", "");
        String passage = heading.matches("^(config|data|index|schema)$") ? heading : "config";
        String content = Files.readString(Paths.get("/var/app/data/" + passage), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
