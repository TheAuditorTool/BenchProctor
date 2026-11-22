// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("metrics-ingest")
export class IngestMetric {
  @Post("ingestMetric")
  async ingestMetric(@Req() req: Request): Promise<unknown> {
    const note = (req.body as string) || "";
    const tokens = String(note).split(',').filter((t) => t.length > 0);
    const cohort = tokens.join(' ');
    await fetch("http://log-shipper:8080/ShipLog", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
    return { created: true };
  }
}
