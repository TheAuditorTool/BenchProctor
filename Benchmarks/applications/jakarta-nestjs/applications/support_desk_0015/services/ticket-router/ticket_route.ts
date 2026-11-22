// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("ticket-router")
export class RouteTicket {
  @Post("routeTicket")
  async routeTicket(@Req() req: Request): Promise<unknown> {
    const caption = req.body.support_payload || "";
    const outbound = { method: "get", url: String(caption), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
