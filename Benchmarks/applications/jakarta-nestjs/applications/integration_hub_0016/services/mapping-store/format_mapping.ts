// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("mapping-store")
export class FormatMapping {
  @Post("formatMapping")
  async formatMapping(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers["user-agent"] as string) || "";
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(wording);
    return new StreamableFile(Buffer.from("<section>" + handshake + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
