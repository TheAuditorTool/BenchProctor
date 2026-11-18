import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RecordConsent } from "./consent_record";
import { AnnotateIndex } from "./annotate_index";
import { ValidateDevice } from "./validate_device";
import { NormalizeSnapshot } from "./normalize_snapshot";
import { RenderSummary } from "./render_summary";
import { SummarizeDevice } from "./summarize_device";
import { AuditThreshold } from "./audit_threshold";
import { VerifyDevice } from "./verify_device";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RecordConsent, AnnotateIndex, ValidateDevice, NormalizeSnapshot, RenderSummary, SummarizeDevice, AuditThreshold, VerifyDevice],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
