// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest10305 {

    @GET
    @Path("/BenchmarkTest10305")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest10305(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        return Response.ok("<div>" + hostValue + "</div>", MediaType.TEXT_HTML).build();
    }
}
