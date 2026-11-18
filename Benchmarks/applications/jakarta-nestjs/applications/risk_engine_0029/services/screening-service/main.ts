import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RunScreening } from "./screening_run";
import { ValidateReceipt } from "./validate_receipt";
import { AuditWindow } from "./audit_window";
import { ReconcileRecord } from "./reconcile_record";
import { EnrichSchedule } from "./enrich_schedule";
import { ValidateManifest } from "./validate_manifest";
import { VerifyIndex } from "./verify_index";
import { CollectWindow } from "./collect_window";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RunScreening, ValidateReceipt, AuditWindow, ReconcileRecord, EnrichSchedule, ValidateManifest, VerifyIndex, CollectWindow],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
