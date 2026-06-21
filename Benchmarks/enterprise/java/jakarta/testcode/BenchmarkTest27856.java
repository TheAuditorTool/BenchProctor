// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest27856 {

    private static String sharedLastValue = "";
    private static int sharedWriteCount = 0;
    private static final Object SHARED_WRITE_LOCK = new Object();

    @GET
    @Path("/BenchmarkTest27856")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest27856(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        synchronized(SHARED_WRITE_LOCK) {
            sharedLastValue = hostValue;
            int seen = sharedWriteCount;
            sharedWriteCount = seen + 1;
        }
        return Response.ok().build();
    }
}
