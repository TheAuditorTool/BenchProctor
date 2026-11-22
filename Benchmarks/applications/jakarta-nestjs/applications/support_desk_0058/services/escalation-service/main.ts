import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RaiseEscalation } from "./escalation_raise";
import { PublishThreshold } from "./publish_threshold";
import { LoadThreshold } from "./load_threshold";
import { LoadEscalation } from "./load_escalation";
import { ResolveSummary } from "./resolve_summary";
import { AuditSchedule } from "./audit_schedule";
import { AuditConfig } from "./audit_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RaiseEscalation, PublishThreshold, LoadThreshold, LoadEscalation, ResolveSummary, AuditSchedule, AuditConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
