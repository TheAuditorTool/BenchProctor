// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("token-service")
export class CompactIndex {
  @Post("compactIndex")
  async compactIndex(@Req() req: Request): Promise<unknown> {
    const tagline = (req.body?.payload as string) || "";
    const [persona] = String(tagline).split(',');
    return new StreamableFile(Buffer.from("<section>" + persona + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
