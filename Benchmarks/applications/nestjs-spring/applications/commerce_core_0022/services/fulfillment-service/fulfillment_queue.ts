// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { UseGuards } from "@nestjs/common";
import { AuthGuard } from "./auth.guard";

@Controller("fulfillment-service")
export class QueueFulfillment {
  @Post("queueFulfillment/:id")
  @UseGuards(AuthGuard)
  async queueFulfillment(@Req() req: Request): Promise<unknown> {
    const subject = (req.params.id as string) || "";
    (globalThis as any).lastRequestValue = subject;
    const voucher: string = (globalThis as any).lastRequestValue;
    await fetch("http://promo-service:8080/ApplyPromo", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: voucher})});
    return { created: true };
  }
}
