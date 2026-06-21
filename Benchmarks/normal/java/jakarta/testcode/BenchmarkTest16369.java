// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest16369 {

    private static final java.util.concurrent.atomic.AtomicReference<String> valueRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GET
    @Path("/BenchmarkTest16369")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16369(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        valueRef.set(headerValue);
        String data = valueRef.get();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        return Response.ok("{\"resource\":\"" + processed + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
