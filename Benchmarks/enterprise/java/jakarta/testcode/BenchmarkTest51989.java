// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest51989 {

    @GET
    @Path("/BenchmarkTest51989")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest51989(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : originValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        response.setHeader("X-Forwarded-For", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
