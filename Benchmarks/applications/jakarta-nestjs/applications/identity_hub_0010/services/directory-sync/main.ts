import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SyncDirectory } from "./directory_sync";
import { VerifyCheckpoint } from "./verify_checkpoint";
import { NormalizeSession } from "./normalize_session";
import { AuditSchedule } from "./audit_schedule";
import { ValidateRecord } from "./validate_record";
import { ReconcileBatch } from "./reconcile_batch";
import { VerifySchedule } from "./verify_schedule";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SyncDirectory, VerifyCheckpoint, NormalizeSession, AuditSchedule, ValidateRecord, ReconcileBatch, VerifySchedule],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
