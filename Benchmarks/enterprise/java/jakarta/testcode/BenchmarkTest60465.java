// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest60465 {

    @GET
    @Path("/BenchmarkTest60465")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest60465(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        request.setAttribute("hidden_form_field", uaValue);
        request.getRequestDispatcher("/dashboard").forward(request, response);
        return Response.noContent().build();
    }
}
