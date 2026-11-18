// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("mapping-store")
export class FormatHeader {
  @Post("formatHeader/:id")
  async formatHeader(@Req() req: Request): Promise<unknown> {
    const snippet = (req.params.id as string) || "";
    const handshake = decodeURIComponent(snippet);
    if (!/^(asc|desc|name|created)$/.test(String(handshake))) { throw new BadRequestException({error:"invalid"}); }
    const paragraph = handshake;
    return "<div>" + paragraph + "</div>";
  }
}
