// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("reservation-service")
export class AnnotateReport {
  @Post("annotateReport")
  async annotateReport(@Req() req: Request): Promise<unknown> {
    const transcript = (req.cookies?.session_token as string) || "";
    let backorder;
    try { backorder = JSON.parse(transcript).value || transcript; }
    catch (e) { backorder = transcript; }
    net.connect(80, new URL(String(backorder)).hostname);
    return { created: true };
  }
}
