import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RouteTicket } from "./ticket_route";
import { ReconcileCheckpoint } from "./reconcile_checkpoint";
import { PruneHeader } from "./prune_header";
import { EnrichBundle } from "./enrich_bundle";
import { ResolveSurvey } from "./resolve_survey";
import { PruneSnapshot } from "./prune_snapshot";
import { ValidateBundle } from "./validate_bundle";
import { PruneReceipt } from "./prune_receipt";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RouteTicket, ReconcileCheckpoint, PruneHeader, EnrichBundle, ResolveSurvey, PruneSnapshot, ValidateBundle, PruneReceipt],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
