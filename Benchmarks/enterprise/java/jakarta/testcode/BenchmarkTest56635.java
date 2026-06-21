// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest56635 {

    private static String stripWhitespace(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest56635")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest56635(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = stripWhitespace(forwardedIp);
        if (!data.matches("^[\\w\\s.\\-:/=\\r\\n]+$")) {
            return Response.status(400).entity("forbidden").build();
        }
        return Response.ok(String.valueOf(data), MediaType.TEXT_HTML).build();
    }
}
