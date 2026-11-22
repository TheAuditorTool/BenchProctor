// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("order-api")
export class PlaceOrder {
  @Post("placeOrder")
  async placeOrder(@Req() req: Request): Promise<unknown> {
    const headline = (req.body?.variables?.input as string) || "";
    const parts: string[] = [];
    for (const token of String(headline).split(',')) { parts.push(token); }
    const backorder: string = parts.join(',');
    await fetch("http://cart-service:8080/UpdateCart", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: backorder})});
    return { created: true };
  }
}
