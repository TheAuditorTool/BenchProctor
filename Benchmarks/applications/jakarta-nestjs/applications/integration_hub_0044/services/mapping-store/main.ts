import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { MapField } from "./field_mapping";
import { FetchRecord } from "./fetch_record";
import { FetchLedger } from "./fetch_ledger";
import { FormatRoster } from "./format_roster";
import { CollectConnector } from "./collect_connector";
import { PublishSummary } from "./publish_summary";
import { ArchiveMapping } from "./archive_mapping";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, MapField, FetchRecord, FetchLedger, FormatRoster, CollectConnector, PublishSummary, ArchiveMapping],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
