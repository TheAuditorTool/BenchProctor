import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { HoldReservation } from "./reservation_hold";
import { FormatHeader } from "./format_header";
import { AnnotateReport } from "./annotate_report";
import { VerifyProfile } from "./verify_profile";
import { ReconcileSchedule } from "./reconcile_schedule";
import { NormalizeSchedule } from "./normalize_schedule";
import { BuildSchedule } from "./build_schedule";
import { LoadReservation } from "./load_reservation";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, HoldReservation, FormatHeader, AnnotateReport, VerifyProfile, ReconcileSchedule, NormalizeSchedule, BuildSchedule, LoadReservation],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
