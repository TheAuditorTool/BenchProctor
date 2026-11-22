import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { EnrollDevice } from "./device_enroll";
import { SummarizeIndex } from "./summarize_index";
import { AnnotateProfile } from "./annotate_profile";
import { SummarizePolicy } from "./summarize_policy";
import { ExportSummary } from "./export_summary";
import { ReconcileSummary } from "./reconcile_summary";
import { RenderSnapshot } from "./render_snapshot";
import { AnnotatePolicy } from "./annotate_policy";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, EnrollDevice, SummarizeIndex, AnnotateProfile, SummarizePolicy, ExportSummary, ReconcileSummary, RenderSnapshot, AnnotatePolicy],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
