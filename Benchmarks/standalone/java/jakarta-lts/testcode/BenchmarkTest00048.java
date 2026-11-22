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
public class BenchmarkTest00048 {

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

    @POST
    @Path("/BenchmarkTest00048")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00048(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data;
        if (rawData.length() > 256) { data = rawData.substring(0, 256); }
        else { data = rawData; }
        javax.xml.xpath.XPath xpath = javax.xml.xpath.XPathFactory.newInstance().newXPath();
        Double matchingUsers = xpath.evaluateExpression("count(/users/user[@name='" + data + "'])", new org.xml.sax.InputSource(new java.io.StringReader("<users><user name=\"alice\" role=\"viewer\"/><user name=\"bob\" role=\"admin\"/></users>")), Double.class);
        response.setHeader("X-User-Count", String.valueOf(matchingUsers));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
