// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest62095 {

    private static final java.util.concurrent.atomic.AtomicReference<String> valueRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GET
    @Path("/BenchmarkTest62095/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest62095(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        valueRef.set(pathValue);
        String data = valueRef.get();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
        }
        return Response.ok().build();
    }
}
