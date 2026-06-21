// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest72599 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest72599")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest72599(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = normalize(forwardedIp);
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
