// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("dunning-service")
export class EnrichSummary {
  @Post("enrichSummary")
  async enrichSummary(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.authorization as string) || "";
    const parts: string[] = [];
    for (const token of String(footnote).split(',')) { parts.push(token); }
    const remittance: string = parts.join(',');
    return new StreamableFile(Buffer.from("<section>" + remittance + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
