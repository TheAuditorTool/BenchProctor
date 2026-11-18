import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { PollTracking } from "./tracking_poll";
import { BuildRecord } from "./build_record";
import { RotateLabel } from "./rotate_label";
import { CompactPolicy } from "./compact_policy";
import { AuditBatch } from "./audit_batch";
import { CollectProfile } from "./collect_profile";
import { CompactThreshold } from "./compact_threshold";
import { ArchiveRecord } from "./archive_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PollTracking, BuildRecord, RotateLabel, CompactPolicy, AuditBatch, CollectProfile, CompactThreshold, ArchiveRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
