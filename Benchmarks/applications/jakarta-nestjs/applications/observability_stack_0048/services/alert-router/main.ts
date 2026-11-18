import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RouteAlert } from "./alert_route";
import { AuditDigest } from "./audit_digest";
import { RotateCheckpoint } from "./rotate_checkpoint";
import { CompactReceipt } from "./compact_receipt";
import { ReconcileSample } from "./reconcile_sample";
import { ExportSchedule } from "./export_schedule";
import { BuildSnapshot } from "./build_snapshot";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RouteAlert, AuditDigest, RotateCheckpoint, CompactReceipt, ReconcileSample, ExportSchedule, BuildSnapshot],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
