// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("order-api")
export class FormatBatch {
  @Post("formatBatch")
  async formatBatch(@Req() req: Request): Promise<unknown> {
    const headline = (req.body.payload as string) || "";
    let backorder;
    try { backorder = JSON.parse(headline).value || headline; }
    catch (e) { backorder = headline; }
    net.connect(80, new URL(String(backorder)).hostname);
    return { created: true };
  }
}
