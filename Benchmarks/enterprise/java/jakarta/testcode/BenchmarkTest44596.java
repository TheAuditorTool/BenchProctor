// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest44596 {

    private static String trimEnds(String v) { return v.trim(); }

    @GET
    @Path("/BenchmarkTest44596")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest44596(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String data = trimEnds(headerValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.setHeader("Access-Control-Allow-Origin", processed);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
