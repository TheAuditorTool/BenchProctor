// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("presence-service")
export class FormatHeader {
  @Post("formatHeader")
  async formatHeader(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body as string) || "";
    const bulletin = String(footnote).split(/[ \t]+/).join(" ");
    http.get(bulletin);
    return { created: true };
  }
}
