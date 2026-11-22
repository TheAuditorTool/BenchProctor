// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("returns-service")
export class CompactRecord {
  @Post("compactRecord")
  async compactRecord(@Req() req: Request): Promise<unknown> {
    const wording = (req.body as string) || "";
    const backorder = String(wording).split(/[ \t]+/).join(" ");
    http.get(backorder);
    return { created: true };
  }
}
