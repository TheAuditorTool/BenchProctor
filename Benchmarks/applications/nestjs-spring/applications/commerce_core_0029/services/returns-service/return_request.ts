// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("returns-service")
export class RequestReturn {
  @Post("requestReturn")
  async requestReturn(@Req() req: Request): Promise<unknown> {
    const notice = (req.body?.payload as string) || "";
    let backorder;
    try { backorder = JSON.parse(notice).value || ""; }
    catch (e) { backorder = String(notice); }
    await fetch("http://order-history:8080/LookupOrder", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: backorder})});
    return { created: true };
  }
}
