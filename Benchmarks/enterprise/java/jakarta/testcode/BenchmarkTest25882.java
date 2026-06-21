// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest25882 {

    @GET
    @Path("/BenchmarkTest25882/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest25882(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = "[%s]".formatted(pathValue);
        return Response.ok(String.valueOf(data), MediaType.TEXT_HTML).build();
    }
}
