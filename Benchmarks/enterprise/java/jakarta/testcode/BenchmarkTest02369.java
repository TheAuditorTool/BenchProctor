// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest02369 {

    private static final java.util.concurrent.atomic.AtomicReference<String> holder = new java.util.concurrent.atomic.AtomicReference<>();

    @GET
    @Path("/BenchmarkTest02369")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest02369(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        holder.set(headerValue);
        String data = holder.get();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        return Response.ok("{\"resource\":\"" + processed + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
