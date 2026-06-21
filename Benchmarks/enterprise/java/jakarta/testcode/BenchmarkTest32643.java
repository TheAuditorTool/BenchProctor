// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest32643 {

    @GET
    @Path("/BenchmarkTest32643")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest32643(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = userId.replace("\u0000", "");
        return Response.ok(String.valueOf(data), MediaType.TEXT_HTML).build();
    }
}
