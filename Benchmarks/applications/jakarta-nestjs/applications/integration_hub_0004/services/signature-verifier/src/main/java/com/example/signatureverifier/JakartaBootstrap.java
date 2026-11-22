package com.example.signatureverifier;

public class JakartaBootstrap {

    @javax.ws.rs.Path("/health")
    public static class HealthResource {
        @javax.ws.rs.GET
        public javax.ws.rs.core.Response health() {
            return javax.ws.rs.core.Response.ok("ok").build();
        }
    }

    public static void main(String[] args) throws Exception {
        java.util.Map<String, String> initParams = new java.util.HashMap<>();
        initParams.put(
            "jersey.config.server.provider.classnames",
            "org.glassfish.jersey.server.filter.RolesAllowedDynamicFeature,org.glassfish.jersey.jackson.JacksonFeature,com.example.signatureverifier.JakartaBootstrap$HealthResource,com.example.signatureverifier.EnrichReport,com.example.signatureverifier.FetchPolicy,com.example.signatureverifier.ReconcileSummary,com.example.signatureverifier.RenderManifest,com.example.signatureverifier.RotateLedger,com.example.signatureverifier.SummarizeLedger,com.example.signatureverifier.ValidateBatch,com.example.signatureverifier.VerifySignature");
        org.glassfish.grizzly.http.server.HttpServer server =
            org.glassfish.jersey.grizzly2.servlet.GrizzlyWebContainerFactory.create(
                java.net.URI.create("http://0.0.0.0:8080/"), initParams);
        server.start();
        Thread.currentThread().join();
    }
}
