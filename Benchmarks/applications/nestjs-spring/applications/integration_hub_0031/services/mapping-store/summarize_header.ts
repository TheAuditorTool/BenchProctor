// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("mapping-store")
export class SummarizeHeader {
  @Post("summarizeHeader")
  async summarizeHeader(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers.authorization as string) || "";
    const handshake = Buffer.from(snippet, "base64").toString();
    return "<div>" + handshake + "</div>";
  }
}
