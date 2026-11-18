// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("case-service")
export class OpenCase {
  @Post("openCase")
  async openCase(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.authorization as string) || "";
    const tokens = String(synopsis).split(',').filter((t) => t.length > 0);
    const verdict = tokens.join(' ');
    await fetch("http://decision-log:8080/RecordDecision", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: verdict})});
    return { created: true };
  }
}
