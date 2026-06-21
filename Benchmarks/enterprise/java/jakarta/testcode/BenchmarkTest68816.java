// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest68816 {

    @GET
    @Path("/BenchmarkTest68816")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest68816(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String prefix = hostValue.length() > 0 ? hostValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = hostValue.toLowerCase(); break;
            case "f": data = hostValue.toUpperCase(); break;
            default: data = hostValue.strip(); break;
        }
        java.util.regex.Pattern inputPattern = java.util.regex.Pattern.compile("[a-zA-Z0-9_-]+");
        if (inputPattern.matcher(data).find()) {
            response.setHeader("X-Validated-Input", data);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
