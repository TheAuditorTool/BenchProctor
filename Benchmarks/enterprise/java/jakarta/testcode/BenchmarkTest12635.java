// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;

@Path("/")
public class BenchmarkTest12635 {

    @GET
    @Path("/BenchmarkTest12635")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest12635(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(headerValue);
        String data = carrier.toString();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            new Socket(data, 80).close();
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
