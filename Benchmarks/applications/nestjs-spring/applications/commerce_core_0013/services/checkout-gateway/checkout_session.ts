// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("checkout-gateway")
export class StartCheckout {
  @Post("startCheckout")
  async startCheckout(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.host as string) || "";
    const parts: string[] = [];
    for (const token of String(wording).split(',')) { parts.push(token); }
    const backorder: string = parts.join(',');
    await fetch("http://returns-service:8080/RequestReturn", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: backorder})});
    return { created: true };
  }
}
