import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { InviteMember } from "./member_invite";
import { AnnotateSummary } from "./annotate_summary";
import { NormalizeRoster } from "./normalize_roster";
import { RotateProfile } from "./rotate_profile";
import { AuditMembership } from "./audit_membership";
import { AnnotatePolicy } from "./annotate_policy";
import { NormalizeRecord } from "./normalize_record";
import { CollectThreshold } from "./collect_threshold";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, InviteMember, AnnotateSummary, NormalizeRoster, RotateProfile, AuditMembership, AnnotatePolicy, NormalizeRecord, CollectThreshold],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
