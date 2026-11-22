// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("digest-service")
export class RenderProfile {
  @Post("renderProfile")
  async renderProfile(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers["x-forwarded-for"] as string) || "";
    const bulletin = footnote != null ? footnote : '';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(bulletin)) { throw new BadRequestException({error:"invalid"}); }
    const snippet = bulletin;
    return "<div>" + snippet + "</div>";
  }
}
