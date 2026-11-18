import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RecordDecision } from "./decision_record";
import { RenderRule } from "./render_rule";
import { PublishReport } from "./publish_report";
import { AuditThreshold } from "./audit_threshold";
import { MergeRoster } from "./merge_roster";
import { VerifyProfile } from "./verify_profile";
import { MergeDigest } from "./merge_digest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RecordDecision, RenderRule, PublishReport, AuditThreshold, MergeRoster, VerifyProfile, MergeDigest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
