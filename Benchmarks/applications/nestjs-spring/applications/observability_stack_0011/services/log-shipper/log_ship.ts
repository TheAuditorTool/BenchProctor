// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("log-shipper")
export class ShipLog {
  @Post("shipLog")
  async shipLog(@Req() req: Request): Promise<unknown> {
    const caption = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const gauge: string = transform(caption);
    await fetch("http://metrics-ingest:8080/IngestMetric", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
    return { created: true };
  }
}
