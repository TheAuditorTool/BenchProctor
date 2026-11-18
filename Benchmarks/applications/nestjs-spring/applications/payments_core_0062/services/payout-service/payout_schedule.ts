// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("payout-service")
export class SchedulePayout {
  @Post("schedulePayout")
  async schedulePayout(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers.referer as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(headline);
    const disbursement: string = readInput();
    await fetch("http://fx-service:8080/ConvertFx", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: disbursement})});
    return { created: true };
  }
}
