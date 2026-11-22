import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RecordBounce } from "./bounce_record";
import { VerifySchedule } from "./verify_schedule";
import { RenderPolicy } from "./render_policy";
import { ArchiveIndex } from "./archive_index";
import { ReconcileBatch } from "./reconcile_batch";
import { EnrichHeader } from "./enrich_header";
import { PublishCheckpoint } from "./publish_checkpoint";
import { AuditLedger } from "./audit_ledger";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RecordBounce, VerifySchedule, RenderPolicy, ArchiveIndex, ReconcileBatch, EnrichHeader, PublishCheckpoint, AuditLedger],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
