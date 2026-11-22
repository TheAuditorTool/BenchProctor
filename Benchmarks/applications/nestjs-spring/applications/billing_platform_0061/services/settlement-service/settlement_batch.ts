// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("settlement-service")
export class RunSettlement {
  @Post("runSettlement")
  async runSettlement(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers["x-forwarded-for"] as string) || "";
    const remittance = footnote != null ? footnote : '';
    await fetch("http://dunning-service:8080/SendDunningNotice", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: remittance})});
    return { created: true };
  }
}
