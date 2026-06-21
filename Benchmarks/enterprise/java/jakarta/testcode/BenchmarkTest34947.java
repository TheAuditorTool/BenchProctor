// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest34947 {

    @GET
    @Path("/BenchmarkTest34947")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest34947(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        StringBuilder bundle = new StringBuilder();
        bundle.append(headerValue);
        String data = bundle.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        return Response.status(500).entity(processed).build();
    }
}
