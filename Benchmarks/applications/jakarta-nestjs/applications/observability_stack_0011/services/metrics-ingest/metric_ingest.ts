// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("metrics-ingest")
export class IngestMetric {
  @Post("ingestMetric")
  async ingestMetric(@Req() req: Request): Promise<unknown> {
    const heading = req.body.telemetry_payload || "";
    JSON.parse(heading);
    return { created: true };
  }
}
