// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("case-service")
export class NormalizeIndex {
  @Post("normalizeIndex")
  async normalizeIndex(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    http.get(summary);
    return { created: true };
  }
}
