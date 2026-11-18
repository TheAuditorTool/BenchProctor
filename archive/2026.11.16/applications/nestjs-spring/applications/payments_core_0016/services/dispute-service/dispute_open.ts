// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("dispute-service")
export class OpenDispute {
  @Post("openDispute")
  async openDispute(@Req() req: Request): Promise<unknown> {
    const passage = (req.cookies?.session_token as string) || "";
    const tokens = String(passage).split(',').filter((t) => t.length > 0);
    const remittance = tokens.join(' ');
    await fetch("http://capture-service:8080/SettleCapture", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: remittance})});
    return { created: true };
  }
}
