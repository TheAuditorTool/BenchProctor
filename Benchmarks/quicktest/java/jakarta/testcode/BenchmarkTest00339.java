// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest00339 {

    @GET
    @Path("/BenchmarkTest00339")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00339(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(headerValue);
        String data = wrapper.toString();
        return Response.status(500).entity(data).build();
    }
}
