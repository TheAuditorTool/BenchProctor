// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest49880 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @GET
    @Path("/BenchmarkTest49880")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest49880(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String data = expandTabs(headerValue);
        return Response.status(500).entity(data).build();
    }
}
