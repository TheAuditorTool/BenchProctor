// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("comment-service")
export class CompactManifest {
  @Post("compactManifest")
  async compactManifest(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers["x-forwarded-for"] as string) || "";
    const synopsis = caption != null ? caption : '';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(synopsis)) { throw new BadRequestException({error:"invalid"}); }
    const snippet = synopsis;
    return "<div>" + snippet + "</div>";
  }
}
