// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("order-history")
export class VerifyWindow {
  @Post("verifyWindow")
  async verifyWindow(@Req() req: Request): Promise<unknown> {
    const citation = (req.cookies?.session_token as string) || "";
    let backorder;
    try { backorder = JSON.parse(citation).value || citation; }
    catch (e) { backorder = citation; }
    net.connect(80, new URL(String(backorder)).hostname);
    return { created: true };
  }
}
