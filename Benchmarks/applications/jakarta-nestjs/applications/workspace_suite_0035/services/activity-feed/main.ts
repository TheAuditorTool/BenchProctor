import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { StreamActivity } from "./activity_stream";
import { LoadIndex } from "./load_index";
import { RotateProfile } from "./rotate_profile";
import { AuditMembership } from "./audit_membership";
import { AnnotatePolicy } from "./annotate_policy";
import { NormalizeRecord } from "./normalize_record";
import { CollectThreshold } from "./collect_threshold";
import { AnnotateSnapshot } from "./annotate_snapshot";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, StreamActivity, LoadIndex, RotateProfile, AuditMembership, AnnotatePolicy, NormalizeRecord, CollectThreshold, AnnotateSnapshot],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
