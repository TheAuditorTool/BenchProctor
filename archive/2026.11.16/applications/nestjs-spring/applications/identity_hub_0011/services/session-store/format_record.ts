// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("session-store")
export class FormatRecord {
  @Post("formatRecord")
  async formatRecord(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers.authorization as string) || "";
    const persona = Buffer.from(excerpt, "base64").toString();
    return "<div>" + persona + "</div>";
  }
}
