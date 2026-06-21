// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest21095 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest21095")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest21095(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = normalize(uaValue);
        return Response.ok(String.valueOf(data), MediaType.TEXT_HTML).build();
    }
}
