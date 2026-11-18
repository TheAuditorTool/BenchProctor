// SPDX-License-Identifier: Apache-2.0
package com.example.revisionstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class RotateSummary {

    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @POST
    @Path("/RotateSummary/graphql")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response rotateSummary(GraphQLRequest req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.util.Properties holder = new java.util.Properties();
        holder.setProperty("value", footnote);
        String byline = holder.getProperty("value", "");
        String addendum = byline.matches("^(config|data|index|schema)$") ? byline : "config";
        String content = Files.readString(Paths.get("/var/app/data/" + addendum), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
