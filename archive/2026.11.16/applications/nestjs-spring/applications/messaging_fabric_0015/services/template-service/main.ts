import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ComposeTemplate } from "./template_compose";
import { VerifySubscription } from "./verify_subscription";
import { PruneSubscription } from "./prune_subscription";
import { ReconcileIndex } from "./reconcile_index";
import { FetchRecord } from "./fetch_record";
import { ResolveIndex } from "./resolve_index";
import { VerifyProfile } from "./verify_profile";
import { VerifySummary } from "./verify_summary";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ComposeTemplate, VerifySubscription, PruneSubscription, ReconcileIndex, FetchRecord, ResolveIndex, VerifyProfile, VerifySummary],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
