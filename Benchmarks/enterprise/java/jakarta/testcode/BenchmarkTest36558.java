// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest36558 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @POST
    @Path("/BenchmarkTest36558/graphql")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest36558(GraphQLRequest req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String prefix = graphqlVar.length() > 0 ? graphqlVar.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = graphqlVar.toLowerCase(); break;
            case "f": data = graphqlVar.toUpperCase(); break;
            default: data = graphqlVar.strip(); break;
        }
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException nfe) {
            return Response.status(400).entity("invalid number").build();
        }
        return Response.ok("{\"status\":\"ok\"}", MediaType.APPLICATION_JSON).build();
    }
}
