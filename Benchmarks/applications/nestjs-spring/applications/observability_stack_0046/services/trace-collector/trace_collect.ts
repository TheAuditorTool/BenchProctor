// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("trace-collector")
export class CollectTrace {
  @Post("collectTrace")
  async collectTrace(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers["user-agent"] as string) || "";
    const [gauge] = String(paragraph).split(',');
    await fetch("http://sampling-config:8080/ConfigureSample", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
    return { created: true };
  }
}
