import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ComposeTemplate } from "./template_compose";
import { AnnotateWindow } from "./annotate_window";
import { NormalizeProfile } from "./normalize_profile";
import { CollectSummary } from "./collect_summary";
import { PruneRoster } from "./prune_roster";
import { ValidateSchedule } from "./validate_schedule";
import { VerifyDelivery } from "./verify_delivery";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ComposeTemplate, AnnotateWindow, NormalizeProfile, CollectSummary, PruneRoster, ValidateSchedule, VerifyDelivery],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
