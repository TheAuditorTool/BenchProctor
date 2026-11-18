import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { UpdatePresence } from "./presence_update";
import { VerifyHeader } from "./verify_header";
import { ExportRoster } from "./export_roster";
import { AnnotateReceipt } from "./annotate_receipt";
import { CollectSchedule } from "./collect_schedule";
import { CompactSchedule } from "./compact_schedule";
import { FetchRecord } from "./fetch_record";
import { AuditSchedule } from "./audit_schedule";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, UpdatePresence, VerifyHeader, ExportRoster, AnnotateReceipt, CollectSchedule, CompactSchedule, FetchRecord, AuditSchedule],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
