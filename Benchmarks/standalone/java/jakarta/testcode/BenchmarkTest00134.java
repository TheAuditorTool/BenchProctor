// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.container.ContainerRequestContext;
import jakarta.ws.rs.container.ContainerRequestFilter;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00134 {

    @Provider
    public static class BindingRestrictionFilter implements ContainerRequestFilter {
        @Override
        public void filter(ContainerRequestContext requestContext) {
            requestContext.getHeaders().remove("X-Internal-Bind");
        }
    }

    @Provider
    public static class FailureMapper implements ExceptionMapper<Exception> {
        @Override
        public Response toResponse(Exception ex) {
            return Response.status(500).entity("request failed").build();
        }
    }

    @GET
    @Path("/BenchmarkTest00134")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00134(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(hostValue)); }
        catch (NumberFormatException e) { data = hostValue; }
        if (!("true".equals(data) || "false".equals(data))) { return Response.status(400).build(); }
        javax.xml.xpath.XPath xpath = javax.xml.xpath.XPathFactory.newInstance().newXPath();
        javax.xml.xpath.XPathExpression roleQuery = xpath.compile("/users/user[@name='" + data + "']/@role");
        String userRole = roleQuery.evaluate(new org.xml.sax.InputSource(new java.io.StringReader("<users><user name=\"alice\" role=\"viewer\"/><user name=\"bob\" role=\"admin\"/></users>")));
        response.setHeader("X-User-Role", userRole);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
