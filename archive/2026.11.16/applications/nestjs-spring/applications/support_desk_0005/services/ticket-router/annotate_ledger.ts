// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("ticket-router")
export class AnnotateLedger {
  @Post("annotateLedger")
  async annotateLedger(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers.host as string) || "";
    const inquiry = `${phrase}`;
    http.get(inquiry);
    return { created: true };
  }
}
