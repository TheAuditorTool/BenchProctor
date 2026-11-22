// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("screening-service")
export class CollectBundle {
  @Post("collectBundle")
  async collectBundle(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers.authorization as string) || "";
    const parts: string[] = [];
    for (const token of String(memo).split(',')) { parts.push(token); }
    const verdict: string = parts.join(',');
    return new StreamableFile(Buffer.from("<section>" + verdict + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
