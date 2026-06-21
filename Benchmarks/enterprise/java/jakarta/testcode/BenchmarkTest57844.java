// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest57844 {

    @GET
    @Path("/BenchmarkTest57844")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest57844(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = hostValue.replace("\u0000", "");
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
