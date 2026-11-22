// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("metrics-ingest")
export class IngestMetric {
  @Post("ingestMetric/:id")
  async ingestMetric(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.params.id as string) || "";
    (globalThis as any).lastRequestValue = excerpt;
    const cohort: string = (globalThis as any).lastRequestValue;
    await fetch("http://sampling-config:8080/ConfigureSample", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
    return { created: true };
  }
}
