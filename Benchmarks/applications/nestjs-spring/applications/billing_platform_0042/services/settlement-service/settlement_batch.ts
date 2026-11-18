// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("settlement-service")
export class RunSettlement {
  @Post("runSettlement")
  async runSettlement(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.host as string) || "";
    const remittance = `${remark}`;
    await fetch("http://payment-gateway:8080/CapturePayment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: remittance})});
    return { created: true };
  }
}
