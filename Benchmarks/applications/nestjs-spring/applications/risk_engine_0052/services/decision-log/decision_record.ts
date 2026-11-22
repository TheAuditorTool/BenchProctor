// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("decision-log")
export class RecordDecision {
  @Post("recordDecision")
  async recordDecision(@Req() req: Request): Promise<unknown> {
    const memo = (req.body as string) || "";
    const verdict = await Promise.resolve(memo).then(String);
    await fetch("http://screening-service:8080/RunScreening", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: verdict})});
    return { created: true };
  }
}
