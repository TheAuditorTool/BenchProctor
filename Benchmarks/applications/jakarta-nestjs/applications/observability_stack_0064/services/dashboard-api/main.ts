import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { QueryDashboard } from "./dashboard_query";
import { ValidateProfile } from "./validate_profile";
import { EnrichReport } from "./enrich_report";
import { AnnotateReceipt } from "./annotate_receipt";
import { FetchSnapshot } from "./fetch_snapshot";
import { SummarizeWindow } from "./summarize_window";
import { FetchSample } from "./fetch_sample";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, QueryDashboard, ValidateProfile, EnrichReport, AnnotateReceipt, FetchSnapshot, SummarizeWindow, FetchSample],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
