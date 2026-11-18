import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { QueryDashboard } from "./dashboard_query";
import { BuildThreshold } from "./build_threshold";
import { EnrichPolicy } from "./enrich_policy";
import { SummarizeReport } from "./summarize_report";
import { SummarizeRoster } from "./summarize_roster";
import { FormatSchedule } from "./format_schedule";
import { PublishHeader } from "./publish_header";
import { FormatBundle } from "./format_bundle";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, QueryDashboard, BuildThreshold, EnrichPolicy, SummarizeReport, SummarizeRoster, FormatSchedule, PublishHeader, FormatBundle],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
