// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("partner-registry")
export class EnrichThreshold {
  @Post("enrichThreshold/:id")
  async enrichThreshold(@Req() req: Request): Promise<unknown> {
    const blurb = (req.params.id as string) || "";
    const handshake = decodeURIComponent(blurb);
    if (!/^(asc|desc|name|created)$/.test(String(handshake))) { throw new BadRequestException({error:"invalid"}); }
    const citation = handshake;
    return "<div>" + citation + "</div>";
  }
}
