import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ProvisionTenant } from "./tenant_provision";
import { AuditThreshold } from "./audit_threshold";
import { ExportRecord } from "./export_record";
import { NormalizeProfile } from "./normalize_profile";
import { ExportWindow } from "./export_window";
import { VerifyCheckpoint } from "./verify_checkpoint";
import { ResolveReport } from "./resolve_report";
import { MergeWindow } from "./merge_window";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ProvisionTenant, AuditThreshold, ExportRecord, NormalizeProfile, ExportWindow, VerifyCheckpoint, ResolveReport, MergeWindow],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
