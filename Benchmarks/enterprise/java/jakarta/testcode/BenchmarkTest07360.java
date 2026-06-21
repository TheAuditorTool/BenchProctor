// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest07360 {

    private enum AllowedValue { PLAIN, MARKDOWN, HTML, TEXT }

    @GET
    @Path("/BenchmarkTest07360")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest07360(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = authHeader.replace("\u0000", "");
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
