// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("promo-service")
export class ApplyPromo {
  @Post("applyPromo")
  async applyPromo(@Req() req: Request): Promise<unknown> {
    const heading = ((req as any).file?.originalname as string) || "";
    const payload = { get value() { return heading; } };
    const voucher = payload.value;
    await fetch("http://order-history:8080/LookupOrder", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: voucher})});
    return { created: true };
  }
}
