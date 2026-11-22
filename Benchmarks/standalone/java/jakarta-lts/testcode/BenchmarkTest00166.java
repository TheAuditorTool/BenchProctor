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
public class BenchmarkTest00166 {

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
    @Path("/BenchmarkTest00166")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00166(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("APP_INPUT")).orElse("");
        String prefix = envValue.length() > 0 ? envValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = envValue.toLowerCase(); break;
            case "f": data = envValue.toUpperCase(); break;
            default: data = envValue.strip(); break;
        }
        record SchemaInput(@jakarta.validation.constraints.Pattern(regexp = "^[a-zA-Z0-9 _.%~\\-]+$") String value) {}
        jakarta.validation.Validator schemaValidator = jakarta.validation.Validation.buildDefaultValidatorFactory().getValidator();
        if (!schemaValidator.validate(new SchemaInput(data)).isEmpty()) { return Response.status(400).entity("schema invalid").build(); }
        javax.xml.xpath.XPath xpath = javax.xml.xpath.XPathFactory.newInstance().newXPath();
        Double matchingUsers = xpath.evaluateExpression("count(/users/user[@name='" + data + "'])", new org.xml.sax.InputSource(new java.io.StringReader("<users><user name=\"alice\" role=\"viewer\"/><user name=\"bob\" role=\"admin\"/></users>")), Double.class);
        response.setHeader("X-User-Count", String.valueOf(matchingUsers));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
