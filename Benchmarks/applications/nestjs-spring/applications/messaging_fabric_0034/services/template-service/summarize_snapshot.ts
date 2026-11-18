// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("template-service")
export class SummarizeSnapshot {
  @Post("summarizeSnapshot")
  async summarizeSnapshot(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body as string) || "";
    const bulletin = String(footnote).split(/[ \t]+/).join(" ");
    http.get(bulletin);
    return { created: true };
  }
}
