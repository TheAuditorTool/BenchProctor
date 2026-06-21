// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest80339 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest80339")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest80339(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String data = normalize(headerValue);
        return Response.ok(String.valueOf(data), MediaType.TEXT_HTML).build();
    }
}
