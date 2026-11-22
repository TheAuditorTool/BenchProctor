// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("rules-service")
export class EvaluateRule {
  @Post("evaluateRule")
  async evaluateRule(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["user-agent"] as string) || "";
    const verdict = excerpt != null ? excerpt : '';
    await fetch("http://watchlist-sync:8080/SyncWatchlist", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: verdict})});
    return { created: true };
  }
}
