// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest10343 {

    @GET
    @Path("/BenchmarkTest10343")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest10343(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : userId.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        if (!data.isEmpty()) throw new Exception("processing error: " + data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
