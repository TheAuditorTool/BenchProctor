// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeUtil from "util";

@Controller("payments-api")
export class AuthorizePayment {
  @Post("authorizePayment")
  async authorizePayment(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers["x-custom-header"] as string) || "";
    const remittance = nodeUtil.format("%s", footnote);
    await fetch("http://capture-service:8080/SettleCapture", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: remittance})});
    return { created: true };
  }
}
