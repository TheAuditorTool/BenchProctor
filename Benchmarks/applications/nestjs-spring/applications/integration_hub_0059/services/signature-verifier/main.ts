import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { VerifySignature } from "./signature_verify";
import { ReconcileWebhook } from "./reconcile_webhook";
import { ValidateProfile } from "./validate_profile";
import { EnrichMapping } from "./enrich_mapping";
import { CollectManifest } from "./collect_manifest";
import { CollectCheckpoint } from "./collect_checkpoint";
import { AuditRoster } from "./audit_roster";
import { ExportDigest } from "./export_digest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, VerifySignature, ReconcileWebhook, ValidateProfile, EnrichMapping, CollectManifest, CollectCheckpoint, AuditRoster, ExportDigest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
