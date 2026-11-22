// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("address-validator")
export class NormalizeIndex {
  @Post("normalizeIndex")
  async normalizeIndex(@Req() req: Request): Promise<unknown> {
    const citation = (req.body.payload as string) || "";
    const consignment = `${citation}`;
    return new StreamableFile(Buffer.from("<section>" + consignment + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
