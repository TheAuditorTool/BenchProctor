import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RegisterPartner } from "./partner_register";
import { ExportDigest } from "./export_digest";
import { ReconcileSnapshot } from "./reconcile_snapshot";
import { RenderSnapshot } from "./render_snapshot";
import { AnnotateDigest } from "./annotate_digest";
import { EnrichThreshold } from "./enrich_threshold";
import { ResolveWindow } from "./resolve_window";
import { VerifyThreshold } from "./verify_threshold";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RegisterPartner, ExportDigest, ReconcileSnapshot, RenderSnapshot, AnnotateDigest, EnrichThreshold, ResolveWindow, VerifyThreshold],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
