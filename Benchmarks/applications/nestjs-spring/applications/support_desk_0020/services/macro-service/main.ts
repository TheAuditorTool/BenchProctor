import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ApplyMacro } from "./macro_apply";
import { PublishEscalation } from "./publish_escalation";
import { NormalizeDigest } from "./normalize_digest";
import { FetchRoster } from "./fetch_roster";
import { NormalizeSnapshot } from "./normalize_snapshot";
import { BuildReceipt } from "./build_receipt";
import { ExportReport } from "./export_report";
import { RenderThreshold } from "./render_threshold";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ApplyMacro, PublishEscalation, NormalizeDigest, FetchRoster, NormalizeSnapshot, BuildReceipt, ExportReport, RenderThreshold],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
