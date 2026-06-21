// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest45990 {

    @GET
    @Path("/BenchmarkTest45990/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest45990(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : pathValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        int result = 100 / Integer.parseInt(data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
