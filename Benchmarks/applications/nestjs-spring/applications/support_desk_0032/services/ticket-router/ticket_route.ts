// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("ticket-router")
export class RouteTicket {
  @Post("routeTicket")
  async routeTicket(@Req() req: Request): Promise<unknown> {
    const note = (req.headers.referer as string) || "";
    const inquiry = note != null ? note : '';
    await fetch("http://knowledge-index:8080/SearchKnowledge", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
    return { created: true };
  }
}
