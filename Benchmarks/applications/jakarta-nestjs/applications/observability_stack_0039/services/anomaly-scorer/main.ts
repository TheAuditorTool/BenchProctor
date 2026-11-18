import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ScoreAnomaly } from "./anomaly_score";
import { RenderSchedule } from "./render_schedule";
import { RenderReport } from "./render_report";
import { EnrichTrace } from "./enrich_trace";
import { ReconcileRoster } from "./reconcile_roster";
import { ExportWindow } from "./export_window";
import { ReconcileBatch } from "./reconcile_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ScoreAnomaly, RenderSchedule, RenderReport, EnrichTrace, ReconcileRoster, ExportWindow, ReconcileBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
