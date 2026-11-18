import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ScheduleJob } from "./job_schedule";
import { AnnotateQuota } from "./annotate_quota";
import { BuildBatch } from "./build_batch";
import { CompactBatch } from "./compact_batch";
import { SummarizeProfile } from "./summarize_profile";
import { AnnotateSchedule } from "./annotate_schedule";
import { BuildIndex } from "./build_index";
import { MergeSnapshot } from "./merge_snapshot";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ScheduleJob, AnnotateQuota, BuildBatch, CompactBatch, SummarizeProfile, AnnotateSchedule, BuildIndex, MergeSnapshot],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
