// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("capture-service")
export class SettleCapture {
  @Post("settleCapture")
  async settleCapture(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers["user-agent"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(memo);
    const ledger: string = readInput();
    await fetch("http://payout-service:8080/SchedulePayout", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: ledger})});
    return { created: true };
  }
}
