import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { BuildManifest } from "./manifest_build";
import { AuditHeader } from "./audit_header";
import { RotateConfig } from "./rotate_config";
import { AuditReport } from "./audit_report";
import { VerifyManifest } from "./verify_manifest";
import { ReconcileThreshold } from "./reconcile_threshold";
import { VerifyCheckpoint } from "./verify_checkpoint";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, BuildManifest, AuditHeader, RotateConfig, AuditReport, VerifyManifest, ReconcileThreshold, VerifyCheckpoint],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
