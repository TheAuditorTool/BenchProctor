// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("partner-registry")
export class LoadWindow {
  @Post("loadWindow")
  async loadWindow(@Req() req: Request): Promise<unknown> {
    const quotation = (req.headers.authorization as string) || "";
    const handshake = Buffer.from(quotation, "base64").toString();
    return "<div>" + handshake + "</div>";
  }
}
