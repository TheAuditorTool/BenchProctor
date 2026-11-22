import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ScheduleJob } from "./job_schedule";
import { BuildHeader } from "./build_header";
import { PublishCheckpoint } from "./publish_checkpoint";
import { AnnotateSnapshot } from "./annotate_snapshot";
import { CollectQuota } from "./collect_quota";
import { MergeProfile } from "./merge_profile";
import { MergeReport } from "./merge_report";
import { BuildSummary } from "./build_summary";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ScheduleJob, BuildHeader, PublishCheckpoint, AnnotateSnapshot, CollectQuota, MergeProfile, MergeReport, BuildSummary],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
