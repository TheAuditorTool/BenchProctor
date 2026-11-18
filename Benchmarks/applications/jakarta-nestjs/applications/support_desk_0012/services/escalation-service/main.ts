import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RaiseEscalation } from "./escalation_raise";
import { LoadThreshold } from "./load_threshold";
import { AuditHeader } from "./audit_header";
import { AuditEscalation } from "./audit_escalation";
import { ValidateCheckpoint } from "./validate_checkpoint";
import { MergeTicket } from "./merge_ticket";
import { BuildHeader } from "./build_header";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RaiseEscalation, LoadThreshold, AuditHeader, AuditEscalation, ValidateCheckpoint, MergeTicket, BuildHeader],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
