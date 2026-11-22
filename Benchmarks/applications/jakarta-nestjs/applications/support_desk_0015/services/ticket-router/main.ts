import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RouteTicket } from "./ticket_route";
import { CollectReceipt } from "./collect_receipt";
import { SummarizeConfig } from "./summarize_config";
import { RenderHeader } from "./render_header";
import { PruneBundle } from "./prune_bundle";
import { ArchiveEscalation } from "./archive_escalation";
import { PruneBatch } from "./prune_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RouteTicket, CollectReceipt, SummarizeConfig, RenderHeader, PruneBundle, ArchiveEscalation, PruneBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
